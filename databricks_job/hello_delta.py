import os
from datetime import date

from delta import DeltaTable, configure_spark_with_delta_pip
from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import col, lit, row_number


def delta_main() -> None:
    session_builder = (
        SparkSession.builder.appName("Hello Delta")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog"
        )
    )

    # When running on cluster:
    # spark = session_builder.getOrCreate()

    # When running locally:
    spark = configure_spark_with_delta_pip(session_builder).getOrCreate()

    data = [
        ("Alice", 1),
        ("Bob", 2),
    ]
    schema = ("name", "id")
    df = spark.createDataFrame(data, schema).coalesce(1)

    data_dir = os.environ.get("DATA_DIR", ".")
    path = f"{data_dir}/hello_delta"

    print("Saving to table")
    df.write.format("delta").save(path)

    table = DeltaTable.forPath(spark, path)
    print("Data in table:")
    table.toDF().show()

    data2 = [
        ("Alice", 2, date(year=1970, month=1, day=2), "delete"),
        ("Bob", 3, date(year=1970, month=1, day=1), "update"),
        ("Bob", 4, date(year=1970, month=1, day=2), "update"),
        ("Pete", 5, date(year=1970, month=1, day=2), "create"),
    ]
    schema2 = ("name", "id", "date", "op")
    df2 = spark.createDataFrame(data2, schema2)
    print(f"Schema of new data:\n{df2.schema}")
    print("New data")
    df2.show()

    print("Deduplicating new data")
    dedup_df = df2.withColumn(
        "rank", row_number().over(Window.partitionBy("name").orderBy(col("date").desc()))
    ).where(col("rank").eqNullSafe(lit(1)))
    print("Deduplicated new data:")
    dedup_df.show()

    print("Upserting into table")
    (
        table.alias("t")
        .merge(dedup_df.alias("s"), "t.name = s.name")
        .whenMatchedDelete(condition="s.op = 'delete'")
        .whenMatchedUpdate(set={"t.name": "s.name", "t.id": "s.id"})
        .whenNotMatchedInsert(values={"t.name": "s.name", "t.id": "s.id"})
        .execute()
    )

    print("Data in table after update:")
    table.toDF().show()


if __name__ == "__main__":
    delta_main()

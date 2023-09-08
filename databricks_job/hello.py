from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import LongType, StringType, StructField, StructType


def create_dataframe(spark: SparkSession) -> DataFrame:
    """A dummy function created just to be able to add a test."""
    schema = StructType([StructField("name", StringType()), StructField("age", LongType())])
    df = spark.createDataFrame(
        data=[("Alice", 30), ("Bob", 40)],
        schema=schema
        # schema=("name", "age")  # just another option for providing the schema
    )
    return df


def main():
    spark = (
        SparkSession.builder.appName("hello PySpark job")
        # No need to specify `master` - Databricks handles that itself
        .getOrCreate()
    )

    df = create_dataframe(spark)

    print(df.schema)
    df.show()


if __name__ == "__main__":
    main()

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, LongType, StructField


def main():
    spark = (SparkSession.builder
             .appName("hello PySpark job")
             # No need to specify `master` - Databricks handles that itself
             .getOrCreate())

    schema = StructType(
        [
            StructField("name", StringType()),
            StructField("age", LongType())
        ]
    )

    df = spark.createDataFrame(
        data=[
            ("Alice", 30),
            ("Bob", 40)
        ],
        schema=schema
        # schema=("name", "age")
    )

    print(df.schema)
    df.show()


if __name__ == '__main__':
    main()

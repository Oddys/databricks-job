from chispa import assert_df_equality
from pyspark.sql.types import StructType, StringType, LongType

from databricks_job.hello import create_dataframe


def test_create_dataframe(spark):
    schema = StructType().add("name", StringType()).add("age", LongType())
    data = [
        ("Bob", 40),
        ("Alice", 30),
    ]

    expected = spark.createDataFrame(data=data, schema=schema)

    actual = create_dataframe(spark)

    assert_df_equality(actual, expected, ignore_row_order=True)

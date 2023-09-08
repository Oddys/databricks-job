from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StringType, IntegerType, ArrayType

from databricks_job.preparation import get_spark_session


def json_main():
    spark = get_spark_session("JSON processing")
    data = [
        (1, """{"name": "Alice", "id": 1}"""),
        (2, """{"name": "Bob", "id": 2}"""),
    ]
    schema = StructType().add("key", IntegerType()).add("value", StringType())
    # json_schema = "name STRING, id INTEGER"
    json_schema = (
        StructType()
        .add("name", StringType())
        .add("id", IntegerType())
        .add("array", ArrayType(elementType=StringType()))
    )
    (
        spark.createDataFrame(data, schema)
        .select(from_json("value", json_schema).alias("parsed_json"))
        .select("parsed_json.*")
        .show()
    )


if __name__ == "__main__":
    json_main()

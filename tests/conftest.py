import pytest
from pyspark.sql import SparkSession


@pytest.fixture
def spark():
    return SparkSession.builder.appName("Spark Testing").getOrCreate()

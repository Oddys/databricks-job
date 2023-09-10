export DATA_DIR=~/PycharmProjects/databricks-job/.data
export SPARK_HOME=~/PycharmProjects/databricks-job/.venv/lib/python3.9/site-packages/pyspark

export hello_delta_path=$DATA_DIR/hello_delta
if [ -d "$hello_delta_path" ]; then
    rm -r "$hello_delta_path"
fi

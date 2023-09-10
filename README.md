# Basic PySpark project for Databricks job

A simple PySpark template for a wheel task creation in Databricks Jobs

Intended for Databricks Runtime 12.2 LTS, i.e. python 3.9.5, spark 3.3.2.

## Execution

### Locally

To run locally from shell `SPARK_HOME` should be set to a directory containing Spark/PySpark 3.3.2.
For convenience, this variable (and any others, e.g., `DATA_DIR` - a local path for writing data) 
could be set via [prepare_env_for_local_run.sh](scripts/prepare_env_for_local_run.sh) file. 

To prepare the local environment (export the variables and cleanup the output directory) 
execute before running your code:

`source scripts/prepare_env_for_local_run.sh`

To run from PyCharm required environment variables could be set in the run configuration.

**_NB!_** When executing `hello_delta.py` make sure the spark session is created via:

`configure_spark_with_delta_pip(session_builder).getOrCreate()`

(Uncomment that line and comment out `session_builder.getOrCreate()`) 

### Cluster
To set environment variables there 2 options. 

Via UI:

1. On the cluster configuration page, click the **Advanced Options** toggle.

2. Click the **Spark** tab.

3. Set the environment variables in the **Environment Variables** field.

See: https://docs.databricks.com/en/clusters/configure.html#env-var

Via init script:

See [init script template](scripts/db_cluster_init_script_TEMPLATE.sh)

_**NB!**_ Shebang is required

_**NB!**_ Executing just `export NAME=VALUE` works for notebooks, but for some reason does not work for jobs
(a set variable is not accessible via `os.environ.get("NAME")`). 
So, for jobs `echo export ... >> /etc/environment` is required.

**_NB!_** When providing an init script from the Workspace make sure the `/Workspace` part 
is not included in the path, i.e. specify `/Users/<user>/path/to/scripts/script.sh` instead of 
`/Workspace/Users/<user>/path/to/scripts/script.sh`

See: https://docs.databricks.com/en/init-scripts/index.html

## Pre commit
Automatically performs configured actions before each commit.

Currently configured:
- `black` (formatting),
- `ruff` (linting - determining and fixing errors),
- `mypy` (type checks)

To enable this behaviour after cloning the repo and installing the dependencies execute:

`pre-commit install`

To trigger manually:

`pre-commit run --all-files`

## Build
To build execute:

`poetry build`

sdist and/or wheel (depending on `--format` option you have provided, default is both) will land in `dist` dir

## Formatting
`black` is added to dev dependencies and can be used as a formatter.

To just display what changes black would have applied:
`black databricks_job tests --diff`

To perform re-formatting:
`black databricks_job tests`

## Testing
For testing `chispa` helper library is used 
(just because it's gotten the most number of stars on Github - https://github.com/MrPowers/chispa)

To run tests with coverage:
`pytest tests/ --cov databricks_job`

## tox
`tox` can be useful for testing the app in managed environments
(i.e. with different versions of Python and/or libraries).

Usage:

`tox`

Can also be used with `poetry`:

```poetry run tox```

To perform a fresh run without `tox` cache:

```rm -rf .tox && tox```

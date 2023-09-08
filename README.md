# Basic PySpark project for Databricks job

A simple PySpark template for a wheel task creation in Databricks Jobs

Intended for Databricks Runtime 12.2 LTS, i.e. python 3.9.5, spark 3.3.2.

To run locally from shell `SPARK_HOME` should be set to a directory containing Spark/PySpark 3.3.2.
For convenience, this variable (and any others, e.g., `DATA_DIR` - a local path for writing data) 
could be set in `.env` file. To export those variables after starting a shell execute:

`source .env`

To run from PyCharm required environment variables could be set in the run configuration.


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

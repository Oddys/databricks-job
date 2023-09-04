# Basic PySpark project for Databricks job

A simple PySpark template for a wheel task creation in Databricks Jobs

Intended for Databricks Runtime 12.2 LTS, i.e. python 3.9.5, spark 3.3.2.

Note. PySpark version in the project must match Spark version in the env
(for PyCharm provide SPARK_HOME env var in the run configuration).

## Build
To build execute:

`poetry build`

sdist and/or wheel (depending on `--format` option you have provided, default is both) will land in `dist` dir

## Testing
For testing `chispa` helper library is used 
(just because it's gotten the most number of stars on Github - https://github.com/MrPowers/chispa)

To run tests with coverage:
`pytest tests/ --cov databricks_job`

## tox

`tox` can be useful for testing the app in managed environments
(i.e. with different versions of Python and/or libraries)
Usage:
`tox`

`tox` can be used with `poetry` by running:

```poetry run tox```

To perform a fresh run without `tox` and `mypy` caches:

```rm -rf .tox .mypy_cache && poetry run tox```

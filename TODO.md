- Consider converting to pandas DataFrames and using pandas built-in testing functionality 
for comparing DataFrames in tests
- Make `hello_delta.py` parameterizable for smooth switching between local / cluster execution. 
(Tried to implement the output directory cleanup in Python, but that didn't work. 
To remove data in dbfs dbutils are needed. So, tried to enable them via adding `databricks-connect` 
as a dependency, but that package clashes with `pyspark` and/or `delta` causing errors during
local run.)

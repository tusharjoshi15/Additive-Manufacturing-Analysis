import sys
print("Python path:", sys.executable)
print("Virtual env active:", 'dissertation_env' in sys.executable)

# Test our installed packages
import polars as pl
print(f"Polars version: {pl.__version__}")
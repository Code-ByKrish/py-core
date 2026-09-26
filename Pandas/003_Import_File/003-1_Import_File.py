import pandas as pd

df = pd.read_json("Pandas/003_Import_File/data.json")
print(df.to_string())
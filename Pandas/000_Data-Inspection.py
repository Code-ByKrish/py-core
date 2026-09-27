import pandas as pd

df = pd.read_csv("Pandas/003_Import_File/data.csv")

# 1.Show first few rows
# print(df.head())

# 2.Show last few rows 
# print(df.tail())

# 3.Show structure of dataset
# df.info()


# 4.Calculate statistical for numeric col
# print(df.describe())

# 5.List all columns
print(df.columns)
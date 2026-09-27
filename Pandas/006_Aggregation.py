import pandas as pd 

df = pd.read_csv("Pandas/003_Import_File/data.csv")

# whole dataframe
# print(df.mean(numeric_only="True"))
# print(df.sum(numeric_only="True"))
# print(df.min(numeric_only="True"))
# print(df.max(numeric_only="True"))
# print(df.count())

# single column
# print(df['Height'].mean())
# print(df['Height'].sum())
# print(df['Height'].min())
# print(df['Height'].max())
# print(df['Height'].count())

#groupby() function

group = df.groupby("Type1")

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].count())
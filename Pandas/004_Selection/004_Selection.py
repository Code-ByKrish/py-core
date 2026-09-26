import pandas as pd

df = pd.read_csv("Pandas/003_Import_File/data.csv",index_col= "Name")

#Selection by column
#print(df["Name"].to_string())
#print(df["Height"].to_string())
#print(df["Weight"].to_string())
#print(df[["Name","Height","Weight"]].to_string())

#selection by rows
# print(df)
# print(df.loc["Bulbasaur"])
# print(df.loc["Pikachu"])
# print(df.loc["Charizard":"Blastoise",["Height","Weight"]].to_string())
print(df.iloc[0:11:2, 0:3])
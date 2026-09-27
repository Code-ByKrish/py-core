import pandas as pd

df = pd.read_csv("Pandas/003_Import_File/data.csv")

# 1.Drop irrelevant columns
# df = df.drop(columns = ["Legendary","No"])
# print(df)

# 2. Handle Missing Data
# df = df.dropna(subset = ["Type2"])
# df = df.fillna({"Type2": "None"})
# print(df.to_string())

# 3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass" : "GRASS",
#                                    "Fire" : "FIRE",
#                                    "Water" : "WATER"})
# print(df.to_string())

# 4. Standardise text
# df["Name"] = df["Name"].str.lower()
# print(df.to_string())

# 5. FiX Data types
# df["Legendary"] = df["Legendary"].astype(bool)
# print(df.to_string())

# 6. Remove Duplicate Entries
df = df.drop_duplicates()
print(df)
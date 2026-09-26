import pandas as pd

df = pd.read_csv("Pandas/003_Import_File/data.csv", index_col = "Name")

pokemon = input("Enter a Pokemon name: ")

try: 
    print(df.loc[pokemon])
except:
    print(f"{pokemon} not found")
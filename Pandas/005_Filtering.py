import pandas as pd

df = pd.read_csv("Pandas/003_Import_File/data.csv")

#filtering = keeping the rows that match a codn
# # tall_pokemon = df[df["Height"] >= 2] 
# # heavy_pokemon = df[df["weight"] > 100] 
# # legendary_pokemon = df[df["Legendary"] == True]
#water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]

ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(ff_pokemon)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("py-core/Pandas/003_Import_File/data.csv")

type_count = df["Type1"].value_counts(ascending = True)

plt.barh(type_count.index, type_count.values,
        color = "lightblue",
        edgecolor = "black")

plt.title("Number of Pokemon by Primary Type")
plt.xlabel("Count")
plt.ylabel("Type")

plt.savefig("pokemon_types.png")
plt.show()
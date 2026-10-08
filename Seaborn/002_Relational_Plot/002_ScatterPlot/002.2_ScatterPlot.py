import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Seaborn/001_Introduction/student_data.csv")

sns.scatterplot(
    data = df,
    x = "Study_Hours",
    y = "Final_Marks",
    hue = "Department",
    alpha = 0.5,
    s =40
    )

plt.title("Study Hours vs Final Marks", fontsize=16)
plt.xlabel("Study Hours", fontsize=12)
plt.ylabel("Final Marks", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.4)

plt.savefig("Seaborn/002_Relational_Plot/002_ScatterPlot/ScatterPlot.png")
plt.show()

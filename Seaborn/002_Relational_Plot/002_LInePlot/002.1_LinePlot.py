import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Seaborn/001_Introduction/student_data.csv")

sns.lineplot(
    data = df,
    x = "Study_Hours",
    y = "Final_Marks",
    marker = "o",
    linewidth = 2,
    color = "blue"
    )

plt.title("Study Hours vs Final Marks", fontsize = 16)
plt.xlabel("Study Hours",fontsize = 12)
plt.ylabel("Final Marks",fontsize = 12)
plt.grid(True,linestyle = "--", alpha = 0.5)

plt.savefig("Seaborn/002_Relational_Plot/002_LInePlot/LinePlot.png")
plt.show()
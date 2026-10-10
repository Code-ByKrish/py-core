import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Seaborn/001_Introduction/student_data.csv")

sns.kdeplot(
    data = df,
    x = "Final_Marks",
    fill = True,
    hue = "Department"
)

plt.title("Distribution of Final Marks")
plt.xlabel("Final Marks")
plt.ylabel("Density")

plt.show()
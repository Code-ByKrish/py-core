import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Seaborn/001_Introduction/student_data.csv")

sns.histplot(
    data=df,
    x="Final_Marks",
    bins=50,
    kde = True
)
plt.title("Distribution of Final Marks")
plt.xlabel("Final Marks")
plt.ylabel("Number of Students")

plt.show()
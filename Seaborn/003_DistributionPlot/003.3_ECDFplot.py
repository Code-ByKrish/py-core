import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Seaborn/001_Introduction/student_data.csv")

sns.ecdfplot(
    data = df,
    x ="Final_Marks"
)

plt.title("ECDF of Final Marks")
plt.xlabel("Final Marks")
plt.ylabel("Proportions of Students")

plt.show()
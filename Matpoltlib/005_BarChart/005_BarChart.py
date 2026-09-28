import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains","Fruits","Vegetables","Protien","Dairy","Sweets"])
values = np.array([4,3,2,5,3,1])

# plt.bar(categories,values,color = "skyblue")
plt.barh(categories,values,color = "skyblue")

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.savefig("005-2_BarChart.png")
plt.show()
import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshman","Sophomores","Juniors","Seniors"]
values = np.array([300,250,275,225])
colors = ["red","yellow","blue","green"]

plt.pie(values, labels = categories,
                autopct = "%1.1f%%",
                colors= colors,
                explode = [0,0,0,0.1],
                shadow=True,
                startangle =90)

plt.title("College Students")
plt.savefig("006_PieChart.png")
plt.show() 
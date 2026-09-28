import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0,1,1,2,3,4,5,6,7,7,8])
y1 = np.array([55,60,65,62,68,70,75,78,82,85,87])

x2 = np.array([0,1,2,2,3,4,5,6,7,8,8])
y2 = np.array([50,58,65,70,72,78,83,88,92,95,97])

plt.scatter(x1,y1,color = "skyblue",
                alpha = 0.5,
                s = 200,
                label = "Class 1")

plt.scatter(x2,y2, color = "orange",
                alpha = 0.5,
                s = 200,
                label = "Class 2")

plt.title("Test Scores")
plt.xlabel("Hour Studied")
plt.ylabel("Grade")
plt.legend()

plt.savefig("007_ScatterGraph.png")
plt.show()
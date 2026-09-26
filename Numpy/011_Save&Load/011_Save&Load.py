import numpy as np

# Save a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])
np.save("data", array)
print("NumPy array was saved!")

# Load the NumPy array
array = np.load("data.npy")
print(array)
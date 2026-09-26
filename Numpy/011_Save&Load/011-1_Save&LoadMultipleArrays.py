import numpy as np


array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([1.1,2.2,3.3,4.4])

np.savez("data2",array1,array2)
print("Numpy array were saved!")

np.savez_compressed("data3",array1,array2)
print("Numpy array were saved!")


arrays = np.load("data2.npz")
print(arrays)

array1 = arrays["arr_0"]
array2 = arrays["arr_1"]
print(array1)
print(array2)
import numpy as np

array = np.zeros(10)
print(array)

array = np.ones((2,3,10))
print(array)

array = np.full((2,3,10),9)
print(array)

array = np.eye(5)
print(array)

array = np.empty((2,3)) #fast alloc : just reserve memory no initialization
print(array)

array = np.arange(1,101)
print(array)

array = np.arange(0,101,0.1) #(start,stop,step)
print(array)

array = np.linspace(0,10,3) #(start,stop,num)
print(array)
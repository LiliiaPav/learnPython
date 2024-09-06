import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print(arr1+arr2)
print(arr1*arr2)


import matplotlib.pyplot as pl
x=np.array([1,2,3,4,5])
y=np.array([1,4,9,16,25])

pl.plot(x, y)
pl.show()
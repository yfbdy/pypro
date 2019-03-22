import numpy as np

arr = np.arange(12).reshape(3,4)

print(arr)

print(arr.sum())

print(arr.sum(axis=0))
print(arr.sum(axis=1))
print(arr.mean())
print(arr.mean(axis=1))
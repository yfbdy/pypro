import numpy as np

n1 = np.arange(6).reshape(2,3)
n2 = np.arange(7,13).reshape(2,3)
print(n1)
print(n2)
print(np.vstack((n1,n2)))
print(np.hstack((n2,n1)))
import numpy as np

t1 = np.arange(6).reshape(2,3)

print(t1,type(t1))

t2 = t1.flatten(order='C')
print(t2)

t3 = t1.flatten(order='F')
print(t3)
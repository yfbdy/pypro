import numpy as np
import random

t1 = np.array([random.random() for i in range(12)]).reshape(3,4)
print(t1)
print(t1.shape)
print(t1.size)
print(t1.itemsize)
print(t1.dtype)

t1[0,0]=np.NAN
print(t1)

print(t1.dtype)
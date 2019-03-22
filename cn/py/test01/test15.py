import numpy as np
import random

t1 = np.arange(12,dtype=int).reshape(3,4)
print(t1,type(t1),t1.dtype)

t2 = t1.astype(np.float32)
print(t2,t2.dtype)

t3 = np.array([random.random() for i in range(12)]).reshape(3,4)
print(t3,t3.dtype)

print(t3.astype(int))
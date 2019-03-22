import numpy as np

t1 = np.arange(24).reshape(4,6)
print(t1)

t1[:,0]=0
print(t1)

t1[3,5]=0
print(t1)

t1[:]=1
print(t1)
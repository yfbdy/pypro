import numpy as np

a = np.arange(9).reshape(3,3)
print(a)

a1 = np.insert(a,0,[0,0,0],axis=0)
print(a1)

a2 = np.insert(a,0,[0,0,0],axis=1)
print(a2)
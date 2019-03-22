import numpy as  np

t1 = np.arange(6).reshape(2,3)
t2 = np.array([0,1,2])
print(t1)
print(t2)
print(t1-t2)
print(t2-t1)
print(t1+t2)
print(t1/t2)
t3 = np.arange(9).reshape(3,3)
print(t1-t3)
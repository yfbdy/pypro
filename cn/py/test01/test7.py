import numpy as  np

t1 = np.arange(9).reshape(3, 3)
print(t1)

print(t1 < 5)
print(t1[t1 < 5])
print(t1[t1 > 5])
t1[t1 > 5] = 5
print(t1)

import numpy as np

t = np.arange(24).reshape(4,6)

t1 = np.where(t<10,0,10)
print(t)
print(t1)
import numpy as np

a = [i**2  for i in range(1,10)]
print(a)

#元组是不行的
b= (i**2 for i in range(1,10))
print(b,type(b))

c=[b]
print(c)

#集合是可以的
d = {i**2 for i in range(1,10)}
print(d)

a2 = [i**2 for i in range(1,10) if i>4]
print(a2)

import random
#d2 = {random.randint(1,100) for i in range(1,10) if len()<10}
#print(d2)

a3 = np.array([random.random() for i in range(10)])
print(a3,a3.dtype)
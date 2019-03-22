import numpy as np

print(np.zeros([2,4]))

print(np.ones([3,5],dtype=int))

print(np.full([2,5],8,dtype=int,order="F"))

print(np.random.randint(1,100,size=(2,4)))
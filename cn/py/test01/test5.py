import numpy as np

t1 = np.arange(24).reshape(4,6)

#print(t1)
#print(t1[2])
#print(t1[0:2])
#print(t1[-2:])

#print(t1[1,:])
#print(t1[1])

#print(t1[1:4,])
#print(t1[[1,3],])
#print(t1[[1,3],2:5])

#print(t1[:,[0,2]])
print(t1[0:3:2,[0,2]])
print(t1[[0,2],[0,2]])
#注意， 0:3:2 不等于 [0,2]
#切片 返回的不是列表，只有当ndarray后面的括号里，有一个是切片的时候，才有读取队列的操作，否则是读取点的操作，
#可以看到第一个是 4个点，第二个只有2个值
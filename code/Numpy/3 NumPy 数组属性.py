import numpy as np 

#ndarray.ndim用于返回数组的维度，等于秩
# a = np.arange(24)
# print(a.ndim)   #a现在只有一个维度
# #现在调整其大小
# b = a.reshape(2,4,3)#b现在拥有三个维度
# print(b.ndim)

#ndarray.shape也可以用于调整数组大小
# a = np.array([[1,2,3],[4,5,6]])
# print(a.shape)
#调整数组大小
# a = np.array([[1,2,3],[4,5,6]])
# a.shape = (3,2)
# print(a)

#reshape
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)
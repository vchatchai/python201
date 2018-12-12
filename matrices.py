
# %%
import sys
import numpy as np

print('Python: {}'.format(sys.version))
print("Numpy: {}".format(np.__version__))
# %%

# define a scalar
x = 6

print(x)
x = np.array((1, 2, 3))
print(x)

# %%
print('Vector Dimensions: {}'.format(x.shape))
print("Vector size:{}".format(x.size))


# %%
x = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x

print("Matrix dimensions: {}".format(x.shape))
print("Matrix size: {}".format(x.size))


# %%
x = np.ones((3, 3))
x

print("Matrix dimensions: {}".format(x.shape))
print("Matrix size: {}".format(x.size))

# %%
x = np.ones((3, 3, 3))
x


print("Tensor dimensions: {}".format(x.shape))
print("Tensor size: {}".format(x.size))


# %%
# indexing
A = np.ones((5, 5), dtype=np.int)
print(A)


A[0, 1] = 2
print(A)

A[:, 0] = 3
print(A)


A[:, :] = 5
print(A)

# assign tensor

# %%
A = np.ones((5, 5, 5), dtype=np.int)

A[:, 0, 0] = 6
print(A)


# %%
A = np.matrix([[1, 2], [3, 4]])
B = np.ones((2, 2), dtype=np.int)
print('A ')
print(A)
print('B ')
print(B )

C = A + B
print("C = A + B")
print(C)


C = A - B 
print("C = A - B")
print(C)

#%%
#the matrix transpose 
A = np.array(range(9))
A = A.reshape(3,3)
print('reshape')
print(A)
print('transpose')
print(A.T)

A = np.array(range(10))
A = A.reshape(2,5)
print("A")
print(A)
B= A.T
print("B = A.T")
print(B)


#%%
#tensors
A = np.ones((3,3,3,3,3,3,3,3,3,3))
print(A.shape)
print(len(A.shape))
print(A.size)

print(A)
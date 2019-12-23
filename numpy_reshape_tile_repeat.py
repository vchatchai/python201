import numpy as np 

print(np.__version__)
a = np.arange(1, 13)

print( f'a => {a}')

print( f'a.reshape(4,3) => {a.reshape(4,3)}')

print(f'a.reshape(4,-1) => {a.reshape(4,-1)}')

print(f'a.reshape(-1,3) => {a.reshape(-1, 3)}')
b = a.reshape(-1,2)
print(f'b = a.reshape(-1,2) => {b}')

print(f'b.reshape(1,-1) => {b.reshape(1,-1)}')

print(f'b.ravel() => {b.ravel()}')

d = np.array([2,1,8])
print(f'd => {d}')

print(f'np.tile(d,3) => {np.tile(d, 3)}')

print(f'np.tile(d,3) => {np.tile(d,(3,1))}')

e = np.array([[1,2], [10,20]])
print(f'e => {e}')

print(f'np.tile(e, 3) => {np.tile(e, 3)}')

print(f'np.tile(e, (5,1)) => {np.tile(e, (5,1))}')


print(f'np.tile(e, (5,2)) => {np.tile(e, (5,2))}')

print(f'np.tile([1,0], 4) => {np.tile([1,0], 4)}')

print(f'np.tile([[1,0],[0,1]], (4,4)) => {np.tile([[1,0],[0,1]], (4,4))}')

print(f'np.repeat(9,3) => {np.repeat(9,3)}')

print(f'np.repeat([10, 15, 20], 2) => {np.repeat([10,15,20], 2)}')
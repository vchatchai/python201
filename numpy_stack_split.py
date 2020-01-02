import numpy as np 


print(np.__version__)

a = np.reshape(np.arange(1,9), (4,2))
print(f"a => {a}")

b = np.reshape(np.arange(1,9) *20, (4,2))
print(f'b => {b}')

print(f'np.vstack((a,b)) => {np.vstack((a,b))}')


c = np.reshape(np.arange(1,9) *11, (4,2))
print(f'c => {c}')

print(f'np.vstack((a,b,c)) => {np.vstack((a,b,c))}')


print(f'np.hstack((a,b)) => {np.hstack((a,b))}')

d = np.hstack((a,b,c))
print(f'np.hstack((a,b,c)) => {d}')


print(f'np.hsplit(d,3) => {np.hsplit(d,3)}')

print(f'np.vsplit(d,2) => {np.vsplit(d,2)}')


a = np.arange(1, 11)
b = np.arange(1, 11) * 50

print(f'a => {a}')
print(f'b => {b}')
print(f'np.hstack((a,b)) => {np.hstack((a,b))} ')

print(f'np.vstack((a,b)) => {np.vstack((a,b))} ')

print(f'np.stack((a,b),1) => {np.stack((a,b),1)} ')
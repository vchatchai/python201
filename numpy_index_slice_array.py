import numpy as np 

print(f'numpy version {np.__version__}')


a = np.arange(10)  * 10
print(f'a => {a}')

print(f'a[5] => {a[5]}')
print(f'a[-1] => {a[-1]}')

print(f'a[:3] => {a[:3]}')

print(f'a[::2] => {a[::2]}')
print(f'a[::-1] => {a[::-1]}')
import numpy as np 

print(np.__version__)

a = np.reshape(np.arange(1,21), (4,5))
print(a)

print(f'a[1] => {a[1]}')

print(f'a[3] => {a[1]}')

print(f'a[-1] => {a[-1]}')


print(f'a[1,2] => {a[1,2]}')
print(f'a[1][2] => {a[1][2]}')

print(list(np.ndenumerate(a)))

print(f'a[0:2] => {a[0:2]}')
    
print(f'a[2:] => {a[2:]}')

print(f'a[:,2] => {a[:,2]}')

print(f'a[2:4,0:2] => {a[2:4,0:2]}')
print(f'a[2:,:2] => {a[2:,:2]}')

print(f'a[:,3:] => {a[:,3:]}')

print(f'a[::2] =>{a[::2]}')
print(f'a[1::2] => {a[1::2]}')
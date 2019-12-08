import numpy as np


print(f'numpy version {np.__version__}')


a = np.array([4, 7, 8, 1])
print(f'a = {a}') 
print(f"a * 10 => {a * 10}")
print(f"a / 5 => {a / 5}")
print(f"a + 2 => {a + 2}")
print(f"a ** 2 => {a ** 2}")
print(f'2*a+10 => {2*a+10}')

import matplotlib.pyplot as plt


plt.plot(a)
# plt.show()

b = np.array([[4,10,2],[10,20,30]])

print(f'b => {b}')
print(f'b * 2 => {b * 2}')

c = np.array([[5,15,20],[7, 5, 3]])
print(f'c => {c}')
print(f'b + c => {b+c}')
print(f'b -c => {b - c}')
print(f'b * c => {b *c }')
print(f'b /c => {b/c}')
print(f'b//c => {b//c}')

print(f'b%c => {b%c}')

print("universal function")
print(f'np.sqrt(b) => {np.sqrt(b)}')
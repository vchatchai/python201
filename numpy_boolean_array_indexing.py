import numpy as np 
print(f'np.__version__ {np.__version__}')
a = np.random.randint(0,100,20)
print(f'a => {a}')

print(f'a % 2 == 0 => {a % 2 == 0}')
print(f'a[ a % 2 == 0] => {a[a%2 == 0]}')
print(f'(a %  2 == 0) & (a > 50) => {(a %  2 == 0) & (a > 50)}')
print(f'a[(a %  2 == 0) & (a > 50)] => {a[(a %  2 == 0) & (a > 50)]}')
print(f'(a%2 == 0 | (a > 50)) => {a%2 == 0 | (a > 50)}')
print(f'a[(a%2 == 0) | (a > 50)] => {a[(a % 2 == 0)| (a > 50)]}')

p = np.random.randint(1, 9999, 100)
print(f'p => {p}')
print(f'p[p%10 == 9] => {p[p%10 == 9]}')

print(f'np.where(p%10 == 9) => {np.where(p%10 == 9)}')


d = np.loadtxt('displ_cty_hwy.csv', delimiter=',')
print(f'd => {d}')
print(f'd[d == 28] => {d[d==28]}')
print(f'np.where(d == 28) => {np.where(d == 28)}')
print(f'd[0, d > 3] => {d[(d[:, 0] > 3) & (d[:,1] > 15)]}')
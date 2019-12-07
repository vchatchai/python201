import numpy as np 

print(np.__version__)

a = [24,35,18,40]
print(a)
b = np.array(a)
print(b)

print("n.ndim {}".format(b.ndim))
print(f"n.shape {b.shape}")

drink = np.array(["mocha", 'water', 'latte', 'espresso', 'coke'],dtype='<U8')
print(drink)


m2 = np.array(['water',20, 'coffe', 50])
print(f"np.array(['water',20, 'coffe', 50]) => {m2}")

hw = np.array([[170,167,159],[70,48,50]])
print(f"np.array([[170,167,159],[70,48,50]]).shape => {hw.shape}")

print(f"np.array([[170,167,159],[70,48,50]]).ndim => {hw.ndim}")
print(f"np.array([[170,167,159],[70,48,50]]).size => {hw.size}")

zero = np.zeros((4,2))
print("np.zero((4,2)) => {}".format(zero))

print('np.ones((5,3)) > {}'.format(np.ones((5,3))))

zero[:] = 9
print('zero[:] = 9 => {}'.format(zero))

e = np.identity(4)
print(f'np.identity(4) => {e}')
print('np.eye(4) => {}'.format(np.eye(4)))


print('np.arange(1,10) => {} '.format(np.arange(1, 10)))

arange = np.arange(1,51)
print(f'np.arange(1,51) => {arange}')
print('np.reshape(arange, (10,5)) {}'.format(np.reshape(arange, (10,5))))
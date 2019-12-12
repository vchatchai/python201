import numpy as np 
print(f'numpy version: {np.__version__}')

np.random.seed(9)
x = np.random.randint(1, 11, 5)

print(f'np.random.randint(1,11,5) => {x}')

print(f'x * 2 => {x*2}')

b = np.array([2,2,2,2,2])

print(f'b => {b}')


print(f'x * np.array([2]) => {x * np.array([2])}')

print(f'repeat(np.array[2], 5) => {np.repeat(np.array([2]), 5) }')


print(f'x * np.repeat(np.array([2]), 5) => {x * np.repeat(np.array([2]), 5)}')


mu = np.mean(x)
std = np.std(x)
z = (x - np.mean(x)) /  np.std(x)

print(f'np.mean(x) => {mu}')
print(f'np.std(x) => {std}')
print(f'np.repeat() = >{np.repeat(mu, 5)}')


print(f'(x - np.mean(x)) /  np.std(x) =>  {z}' )


#2-dim

a  = np.arange(1, 7).reshape(3, -1 ) * 10

print(f'a => {a}')
print(f'a.shape => {a.shape}')


print(5 + a)

# np.full((3,2), 5)
b = np.full(a.shape, 5)


print(f'b => {b}')

print(f'b + a => {b + a}')

c = np.array([2,10])
print(f'c => {c}')

print(f'a.shape => {a.shape}')
print(f'b.shape => {c.shape}')

print(f'a + c => {a + c}')

# print(f'np.tile(c, a.shape[0]) => {np.tile(c, a.shape([0])).reshape()}')


d=np.array([[2],[3],[4]])
print(f'd => {d}')
 
print(f'a + d => {a + d}')

e = np.array([[5],[100]])
print(f'e => {e}')

print(f'a.shape => {a.shape}')
print(f'e.shape => {e.shape}')
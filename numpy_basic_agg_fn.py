import numpy as np 
print(f'numpy version = {np.__version__}')

w = np.array([70,48, 52, 60, 52])
print(f'w => {w}')
print(f'w.size => {w.size}')
print(f'np.min(w) => {np.min(w)}')
print(f'np.max(w) => {np.max(w)}')
print(f'np.sum(w) => {np.sum(w)}')
print(f'np.mean(w) => {np.mean(w)}')
print(f'np.median(w) => {np.median(w)}')
print(f'np.sort(w) => {np.sort(w)}')

from scipy import stats


m = stats.mode(w)
print(f'stats.mode(w) => {m}')
print(f'm[0] => {m[0]}')
print(f'm[0][0] => {m[0][0]}')

print(f'm[1] => {m[1]}')
print(f'm[1][0] => {m[1][0]}')
print(f'np.sort(w)[::-1] => {np.sort(w)[::-1]}')
w.sort()
print(f'w.sort() => {w} #inplace')

a = np.reshape(np.arange(1,21), (4,5))
print(f'np.reshape(np.arange(1,21), (4,5)) => {a}')
print(f'np.mean(a) => {np.mean(a)}')
print(f'a.size => {a.size}')
print(f'a.shape => {a.shape}')
print(f'np.mean(a[0]) => {np.mean(a[0])}')
print(f'np.mean(a[:,1]) => {np.mean(a[:, 1])}')
print(f'np.mean(a, axis=0) => {np.mean(a, axis=0)}')
print(f'np.sum(a, axis=0) => {np.sum(a, axis=0)}')
print(f'np.sum(a, axis=1) => {np.sum(a, axis=1)}')
print(f'np.std(a) => {np.std(a)}')
print(f'np.var(a) => {np.var(a)}')
print(f'np.ptp(a) => {np.ptp(a)} # peak to peak  np.max(a) - np.min(a) => {np.max(a) - np.min(a)} ')


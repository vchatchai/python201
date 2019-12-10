import numpy as np

idcard = '1101234567897'
idcard = np.array(list(idcard[:]), dtype=int)

order = np.arange(13,1, -1)

# order = np.flip(order)
print(f'order => {order}')

print(f'order.__len__:{order.__len__()}')

idcard = idcard[:idcard.__len__()-1] 
print(f'idcard {idcard}')
result = idcard * order

print(result)

result  = np.sum(result) 
print(result)
result  = np.mod(result, 11)


if result <= 1 : 
    result = 1 - result 
else :
    result = 11 - result

print(result)
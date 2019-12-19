import numpy as np 


valueString = '400638133393'

weightString = '131313131313'

# value = np.array([int(x) for x in valueString])
# weight = np.array([int(x) for x in weightString])

value = np.array(list(valueString[:]), dtype=int)
weight = np.tile([1,3],6)

print(value)
print(weight)
result = value * weight

print(result)
sum =np.sum(result)
print(sum)

mod = 10 - sum%10
print(mod)
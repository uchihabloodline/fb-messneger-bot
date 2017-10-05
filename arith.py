#script for mathematical function

import math

#returns upper or ceil value
print(math.ceil(223.1))

#returns floor value
print(math.floor(17.6))

#returns absolute value
print(math.fabs(-234))

#fatorial function
print(math.factorial(3))
#-------------

#sign gets copies to the first number written
print(math.copysign(12,11))

#returns mod of value entered 
print(math.fmod(12,6))
print(math.fmod(12,65))

#function of fsum

val = [12,33,4,3,3,3,3,3,3,1]

print(math.fsum(val))

res = math.fsum(val)
print(res)
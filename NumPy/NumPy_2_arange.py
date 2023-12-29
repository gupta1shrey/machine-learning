import numpy as np

"""
1- array() - create array from lists or tuples
2- arange() - create array of evenly spaced values
3- zeros()
4- ones()
5- linspace()
6- eye()
7- random()
help(np.array) - know every thing about the array
"""

a = np.arange(1, 10)#a normal arange array
print(a)

a1 = np.arange(5.0)#take first value as none(0)
print(a1)

a2 = np.arange(1, 10, 2)#gives an gaph between numbers 
print(a2)

a3 = np.arange(30, dtype= "str")#set data type(inetial = int)
print(a3)

a4 = np.arange(40, dtype="float")
print(a4)




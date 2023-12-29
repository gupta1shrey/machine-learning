import numpy as np

"""
1- array() - create array from lists or tuples
2- arange() - create array of evenly spaced values
3- zeros() - crates array filled with 0
4- ones() - crates array filled with 0
5- linspace() - create array with evenly spaced value
6- eye()
7- random()
help(np.ones) - know every thing about the array
"""
help(np.linspace)

a = np.linspace(1, 100, num= 10)#make array from 1 to 100 with equal spacing
print(a)

a1 = np.linspace(1, 100, num=10, endpoint=False)#make array with end point
print(a1)

a2 = np.linspace(1, 100, num=10, retstep=True)
print(a2)

a3 = np.linspace(1,100, num=10, dtype="int")#change data type
print(a3)

a4 = np.linspace(1,100)#did not give space
print(a4)

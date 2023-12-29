import numpy as np

"""
1- array() - create array from lists or tuples
2- arange() - create array of evenly spaced values
3- zeros() - crates array filled with 0
4- ones() - crates array filled with 0
5- linspace()
6- eye()
7- random()
help(np.ones) - know every thing about the array
"""

a = np.ones(5)#create array with 1, default data type = float
print(a)

a1 = np.ones(3, dtype=  "int")#change data type
print(a1)

a2 = np.ones((5, 7))#make mutli dimentioal array
print(a2)

a3 = np.ones([4, 6])#make multi dimentional array 
print(a3)
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

a = np.eye(5)#gives array made with 0, with default digonal with 1
print(a)

a1 = np.eye(5, k=-1)#change the place of digonal 
print(a1)
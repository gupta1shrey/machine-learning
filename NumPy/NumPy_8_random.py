import numpy as np

"""
1- array() - create array from lists or tuples
2- arange() - create array of evenly spaced values
3- zeros() - crates array filled with 0
4- ones() - crates array filled with 0
5- linspace() - create array with evenly spaced value
6- eye()
7- random() - 
help(np.ones) - know every thing about the array
"""

a = np.random.rand(10)#creates an array of specified shape and fills it with random values.
print(a)

a1 = np.random.rand(10, 20)#create 2D array with random numbers
print(a1)

a2 = np.random.rand(10, 20, 30)#create 3D array with random numbers
print(a2)

a3 = np.random.randn(10)#create 1D array with random numbers
print(a3)

a4 = np.random.randn(10, 10)#create 2D array with random numbers
print(a4)

a5 = np.random.randn(10, 10, 10)#create 3D array with random numbers
print(a5)

a6 = np.random.ranf(10)#ceate random float value
print(a6)

a7 = np.random.randint(0, 1000)#randomly chose int between given numbers
print(a7)

a8 = np.random.randint(-1, -1000)#randomly chose int between given numbers
print(a8)

a9 = np.random.randint(-1, 1000)#randomly chose int between given numbers
print(a9)




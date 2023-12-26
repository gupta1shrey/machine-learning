import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [4, 5, 6, 7], "g+-", linewidth=15, zorder =1)
plt.plot([1, 2, 3, 4], [4, 5, 8, 10], "r+-", linewidth=15, zorder =2)#zorder = arange
plt.title("graph")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

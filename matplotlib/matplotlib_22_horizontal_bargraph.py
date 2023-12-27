import matplotlib.pyplot as plt

y = ["sci", "eng", "math", "sst", "san", "atl", "hindi"]
w = [200, 100, 200, 175, 75, 200, 150]

plt.barh(y,w, 0.1, color="red", alpha = 0.5, left=[10,10,10,10,10,10,10])#, width=0.1, alpha=0.5, label=1, align="center", edgecolor="red"
plt.legend()


plt.show()
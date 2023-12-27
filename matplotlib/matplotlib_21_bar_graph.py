import matplotlib.pyplot as plt

x = ["sci", "eng", "math", "sst", "san", "atl", "hindi"]
y = [200, 100, 200, 175, 75, 200, 150]

plt.bar(x,y, color="red", width=0.1, alpha=0.5, label=1, align="center", edgecolor="red")
plt.legend()
plt.annotate("bargraph", ["sci", 200], ["sci", 175])

plt.show()
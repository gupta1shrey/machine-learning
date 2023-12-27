import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6], "g+-",  marker = 'o', ms = 20, mec = 'r')
plt.title("graph", {"size" : 40, "color" : "red"}, alpha = 0.7, family = "monospace", style="italic")
plt.xlabel("x label", {"size" : "20", "color" : "green"}, labelpad=10)
plt.ylabel("y label", {"size" : "20", "color" : "green"}, labelpad=10)
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.minorticks_on()
plt.grid(color = "red", which="minor", axis="x")
plt.grid(color = "green", axis="y", which="minor")
plt.show()
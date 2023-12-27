import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6], label = 1)
plt.plot([1, 2, 3], [4, 10, 6], label = 2)
#plt.title("graph", {"size" : 40, "color" : "red"}, alpha = 0.7, family = "monospace", style="italic")
plt.xlabel("x label", {"size" : "20", "color" : "green"}, labelpad=10)
plt.ylabel("y label", {"size" : "20", "color" : "green"}, labelpad=10)
#plt.legend(framealpha = 1, markerfirst=False, shadow=True, frameon=False, ncol = 4, columnspacing = 100, title = "legend", title_fontsize=10)
plt.legend(title = "my label", title_fontsize = "x-large", borderpad = 5, labelspacing = 5)
#plt.minorticks_on()
#plt.grid(color = "red", which="minor", axis="x")
#plt.grid(color = "green", axis="y", which="minor")
plt.show()
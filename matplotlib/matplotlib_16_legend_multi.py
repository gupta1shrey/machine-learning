import matplotlib.pyplot as plt

l1, = plt.plot([1, 2, 3], [4, 5, 6], color="red")
l2, = plt.plot([1, 2, 3], [4, 10, 6], color="green")
l3, = plt.plot([1, 2, 3], [4, 10, 7], color="green")
l4, = plt.plot([1, 2, 3], [6, 2, 13], color="black")
#plt.title("graph", {"size" : 40, "color" : "red"}, alpha = 0.7, family = "monospace", style="italic")
plt.xlabel("x label", {"size" : "20", "color" : "green"}, labelpad=10)
plt.ylabel("y label", {"size" : "20", "color" : "green"}, labelpad=10)
#plt.legend(framealpha = 1, markerfirst=False, shadow=True, frameon=False, ncol = 4, columnspacing = 100, title = "legend", title_fontsize=10)
legend1 = plt.legend((l1,l2),["label1", "label2"],loc="lower right")
plt.gca().add_artist(legend1)
plt.legend((l3,l4),["label3", "label4"])
#plt.legend(title = "my label", title_fontsize = "x-large", borderpad = 5, labelspacing = 5)
#plt.minorticks_on()
#plt.grid(color = "red", which="minor", axis="x")
#plt.grid(color = "green", axis="y", which="minor")
plt.show()
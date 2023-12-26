import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6], "g+-",  marker = 'o', ms = 20, mec = 'r')
plt.title("graph")
plt.xlabel("x label", {"size" : "20", "color" : "green"}, labelpad=10, alpha = 0.4, backgroundcolor ="blue", style = "italic", family = "monospace")
plt.ylabel("y label", {"size" : "20", "color" : "green"}, labelpad=10, alpha = 0.4, backgroundcolor ="blue")
plt.show()



"""
fontname

'serif'
'sans-serif'
'cursive'
'fantasy'
'monospace'
"""








"""
forntsize:

xx-small
x-small
small
medium
large
x-large
xx-large
"""
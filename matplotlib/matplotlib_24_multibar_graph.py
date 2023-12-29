import matplotlib.pyplot as plt
import numpy as np
w=0.4
x = [200, 300, 400, 500, 600, 700, 800]
y = [200, 100, 200, 175, 75, 200, 150]
v = [200, 100, 200, 175, 75, 200, 150]
bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]

plt.bar(bar1,y,w, label="11")
plt.bar(bar2,v,w,label="11")

plt.show()
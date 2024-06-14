import matplotlib.pyplot as plt

x= [1,2,3]
y = [1,2,3]
colour1 = ["red", "green", "blue"]
labels1= ["2001", "2002", "2003"]
plt.title("car sale")
plt.xlabel("year")
plt.ylabel("sale")

plt.bar(x,y, color=colour1, labels = labels1)
plt.show()
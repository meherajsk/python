import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y, color = 'red')
plt.show()



"""
The bar() function takes arguments that describes the layout of the bars.
The categories and their values represented by the first and second argument as arrays.
"""

#Three lines to make our compiler able to draw:

x = ["APPLES", "BANANAS"]
y = [400, 350]

plt.bar(x, y, width = 0.1)
plt.show()



x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()

#The default height value is 0.8




x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()




"""pie cahrt"""
y = np.array([35, 25, 25, 15])

plt.pie(y, startangle=90)
plt.show() 


y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, colors = mycolors)
plt.legend(title = "Four Fruits:")
plt.show() 

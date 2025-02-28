import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.grid() #important
plt.show()

m = np.array([80, 85, 91, 95, 100, 105, 110, 115, 120, 125])
n = np.array([240, 250, 267, 270, 280, 290, 300, 310, 320, 330])
plt.plot(m, n)
#plt.grid(axis ='x') #important you have to specify the axis
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5, axis = 'y') #important
plt.show()


"""
plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

"""

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()






x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title("SALES 1")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)
plt.title("SALES 2")

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)
plt.title("SALES 3")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)
plt.title("SALES 4")

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)
plt.title("SALES 5")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.title("SALES 6")

plt.suptitle("MY SHOP")
plt.show()


# Most of the Matplotlib utilities lies under the pyplot submodule, 
# and are usually imported under theplt alias:

import matplotlib.pyplot as plt
import numpy as np
'''
x = np.array([0, 6, 7, 14, 20])
y = np.array([0, 250, 23, 340, 60])

plt.plot(x, y) #prints line
plt.plot(x, y, "o") #prints only points not line
plt.show()


# marker : you can use the keyword to emphasize each point with aspecified marker
z = np.array([3, 8, 1, 10])
plt.plot(z, marker = '*')
plt.plot(z, marker = 'o')
plt.show()

"""
Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
"""

#marker|line|color


ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o-.r')
plt.show()

"""
Line    Syntax	Description

'-'	    Solid line	
':'	    Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line



Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
"""

#You can use the keyword argument markersize or the shorter version, 
# ms to set the size of the markers:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 15)
plt.show()


#You can use the keyword argument markeredgecolor or the 
# shorter mec to set the color of the edge of the markers:

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()


#You can use the keyword argument markerfacecolor or the 
# shorter mfc to set the color inside the edge of the markers:

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()




"""both"""
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()



...
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
...
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()



y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)

plt.show()

'''


"""label"""

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Sports Watch Data", loc ='left', fontdict = font1) #important
plt.xlabel("Average Pulse", fontdict = font2 ) #important
plt.ylabel("Calorie Burnage", fontdict =font2) #important
plt.show()
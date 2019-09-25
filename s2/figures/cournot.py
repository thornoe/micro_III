# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
import os

# Set working folder
os.chdir('C:/Users/thorn/Onedrive/Dokumenter/GitHub/micro_III/s2/figures')

# Cournot equilibrium: Graphical solution
w = 6 # figure width
fig, ax = plt.subplots(figsize=(w,w/1.62)) # create new figure
x = np.arange(0, 10) # x values
y1 = 9 - 2*x # line 1 points
y2 = (9-x)/2 # line 2 points
ne = set(y2).intersection(y1)
plt.plot(x, y1, label = "BR function for firm 1") # plotting the line 1 points
plt.plot(x, y2, label = "BR function for firm 2") # plotting the line 2 points
ax.set_xlim([0,10]) # x range
ax.set_ylim([0,10]) # y range
plt.xlabel('Output of firm 1') # naming the x axis
plt.ylabel('Output of firm 2') # naming the y axis
plt.legend() # add the legend
fig.savefig('br.pdf', bbox_inches='tight') # save the plot to working folder
plt.show() # show the plot

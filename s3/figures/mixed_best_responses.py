# importing the required modules
import os
import matplotlib.pyplot as plt

# Set working folder (replace backslashes with standard slashes)
os.chdir('C:/Users/jwz766/Documents/GitHub/micro_III/s3/figures') # work pc
os.chdir('C:/Users/thorn/Onedrive/Dokumenter/GitHub/micro_III/s3/figures') # home pc

# Run to update font size again after creating the first figure:
plt.rcParams.update({'font.size': 23})

##############################################################################
#   Mixed best responses in a "(p,q)-diagram"                                #
##############################################################################
# Ex. 5.a
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,1,1], [0,0,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('7a1.pdf', bbox_inches='tight') # save the first plot to working folder
plt.plot([0,0,1], [0,1,1], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([0,1], [0,1], 'kX', markersize=18, label="$NE$") # plotting the PSNE points
plt.legend(bbox_to_anchor=(-.21, 1.02, 1.21, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('7a2.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot

# Ex. 5.b
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,1,1], [0,0,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
    loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('7b1.pdf', bbox_inches='tight') # save the first plot to working folder
plt.plot([0,0,0.99,0.99], [0,4/7,4/7,1], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([0], [0], 'ks', markersize=8) # plotting the PSNE point
plt.plot([1.01,1.01], [4/7,1], 'k', ls='dotted', lw=5, label="$NE$") # plotting the MSNE line
plt.legend(bbox_to_anchor=(-.21, 1.02, 1.21, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('7b2.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot

# Ex. 5.c
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,0,1], [0,1,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('7c1.pdf', bbox_inches='tight') # save the first plot to working folder
plt.plot([0.01,0.01,1], [0,0.99,0.99], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([-0.01,-0.01,1], [0,1.01,1.01], 'k', ls='dotted', lw=5, label="$NE$") # plotting the MSNE line
plt.legend(bbox_to_anchor=(-.21, 1.02, 1.21, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('7c2.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the plot

# Ex. 5.d
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,1/2,1/2,1], [0,0,1,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.xlabel('q (probability of $t_1$)', color='b') # naming the x axis
plt.ylabel('$p_1$ (probability of $s_1$)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('7d1.pdf', bbox_inches='tight') # save the first plot to working folder
plt.plot([0,0,1,1], [0,1/2,1/2,1], 'b', ls='dashed', label="$BR_2(p_1)$") # plotting the line 2 points
plt.plot([0,1/2,1], [0,1/2,1], 'kX', markersize=18, label="$NE$") # plotting the PSNE points
plt.legend(bbox_to_anchor=(-.21, 1.02, 1.21, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('7d2.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot

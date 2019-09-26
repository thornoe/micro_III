# importing the required modules
import os
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})

# Set working folder (replace backslashes with standard slashes)
os.chdir('C:/Users/jwz766/Documents/GitHub/micro_III/s3/figures')
os.chdir('C:/Users/thorn/Onedrive/Dokumenter/GitHub/micro_III/s3/figures')

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
fig.savefig('5a1.pdf', bbox_inches='tight') # save the first plot to working folder
plt.plot([0,0,1], [0,1,1], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([0,1], [0,1], 'kX', markersize=18, label="$NE$") # plotting the PSNE points
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('5a2.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot

# Ex. 5.b
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,1,1], [0,0,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
    loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('5b1.pdf', bbox_inches='tight') # save the first plot to working folder
plt.plot([0,0,0.99,0.99], [0,4/7,4/7,1], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([0], [0], 'ks', markersize=8) # plotting the PSNE point
plt.plot([1.01,1.01], [4/7,1], 'k', ls='dotted', lw=5, label="$NE$") # plotting the MSNE line
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('5b2.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot

# Ex. 5.c
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,0,1], [0,1,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('5c1.pdf', bbox_inches='tight') # save the first plot to working folder
plt.plot([0.01,0.01,1], [0,0.99,0.99], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([-0.01,-0.01,1], [0,1.01,1.01], 'k', ls='dotted', lw=5, label="$NE$") # plotting the MSNE line
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('5c2.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the plot

# Ex. 5.d
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,1/2,1/2,1], [0,0,1,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.xlabel('q (probability of $t_1$)', color='b') # naming the x axis
plt.ylabel('$p_1$ (probability of $s_1$)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('5d1.pdf', bbox_inches='tight') # save the first plot to working folder
plt.plot([0,0,1,1], [0,1/2,1/2,1], 'b', ls='dashed', label="$BR_2(p_1)$") # plotting the line 2 points
plt.plot([0,1/2,1], [0,1/2,1], 'kX', markersize=18, label="$NE$") # plotting the PSNE points
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
fig.savefig('5d2.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot

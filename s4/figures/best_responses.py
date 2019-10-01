# importing the required modules
import os
import matplotlib.pyplot as plt

# Set working folder (replace backslashes with standard slashes)
os.chdir('C:/Users/jwz766/Documents/GitHub/micro_III/s4/figures') # work pc
os.chdir('C:/Users/thorn/Onedrive/Dokumenter/GitHub/micro_III/s4/figures') # home pc


##############################################################################
#   Ex. 1: Mixed best-response functions in a "(p,q)-diagram                 #
##############################################################################
# Ex. 1.a
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,4/7,4/7,1], [0,0,1,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.plot([0,0,1,1], [0,4/7,4/7,1], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([0,4/7,1], [0,4/7,1], 'kX', markersize=18, label="$NE$") # plotting the PSNE points
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
plt.rcParams.update({'font.size': 18}) # update font size
fig.savefig('1a.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot

# Ex. 1.b
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,1,1], [0,0,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.plot([0,0,.99,.99], [0,1/2,1/2,1], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([0], [0], 'ks', markersize=8) # plotting the PSNE point
plt.plot([1.01,1.01], [1/2,1], 'k', ls='dotted', lw=5, label="$NE$") # plotting the MSNE line
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
plt.rcParams.update({'font.size': 18}) # update font size
fig.savefig('1b.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot


##############################################################################
#   Ex. 1: True and false BR functions for a Kahoot quiz                     #
##############################################################################
f, axs = plt.subplots(2,2,figsize=(12,12))
### Ex. 1.a (true) ###
ax1 = plt.subplot(221) # add 1st figure in a 2x2 plot
plt.plot([0,4/7,4/7,1], [0,0,1,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.plot([0,0,1,1], [0,4/7,4/7,1], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([0,4/7,1], [0,4/7,1], 'ks', markersize=8, label="$NE$") # plotting the PSNE points
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
# plt.setp(ax1.get_xticklabels(), visible=False) # make x tick labels invisible
### Ex. 1.a (dummy!) ###
ax2 = plt.subplot(222, sharex=ax1, sharey=ax1) # add 2nd figure in a 2x2 plot, shared x and y
plt.plot([0,4/7,4/7,1], [0,0,1,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.plot([0,3.93/7,3.93/7,1], [.01,.01,1.01,1.01], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([0,4.07/7,4.07/7,1], [-.01,-.01,.99,.99], 'k', ls='dotted', lw=5, label="$NE$") # plotting the MSNE line
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(-.7, 1.02, 1.2, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
# plt.setp(ax2.get_xticklabels(), visible=False) # make x tick labels invisible
# plt.setp(ax2.get_yticklabels(), visible=False) # make y tick labels invisible
### Ex. 1.b (dummy!) ###
ax3 = plt.subplot(223, sharex=ax1, sharey=ax1) # add 3rd figure in a 2x2 plot, shared x and y
plt.plot([0,1,1], [0,0,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.plot([0,1/2,1/2,1], [0.01,0.01,1.01,1.01], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([1], [1.01], 'ks', markersize=8) # plotting the PSNE point
plt.plot([0,1/2], [-.01,-.01], 'k', ls='dotted', lw=5, label="$NE$") # plotting the MSNE line
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
### Ex. 1.b (true) ###
ax4 = plt.subplot(224, sharex=ax1, sharey=ax1) # add 4th figure in a 2x2 plot, shared x and y
plt.plot([0,1,1], [0,0,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.plot([0,0,.99,.99], [0,1/2,1/2,1], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([0], [0], 'ks', markersize=8) # plotting the PSNE point
plt.plot([1.01,1.01], [1/2,1], 'k', ls='dotted', lw=5, label="$NE$") # plotting the MSNE line
plt.xlabel('q (probability of L)', color='b') # naming the x axis
# plt.setp(ax4.get_yticklabels(), visible=False) # make y tick labels invisible
plt.rcParams.update({'font.size': 18}) # update font size
f.savefig('1_kahoot.png', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot


##############################################################################
#   Ex. 3: Mixed best-response functions in a "(p,q)-diagram                 #
##############################################################################
# Ex. 3.b
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,1/2,1/2,1], [1,1,0,0], 'r', label="$BR_A(q)$") # plotting the line 1 points
plt.plot([0,0,1,1], [0,1/2,1/2,1], 'b', ls='dashed', label="$BR_T(p)$") # plotting the line 2 points
plt.plot([1/2], [1/2], 'kX', markersize=18, label="$NE$") # plotting the PSNE points
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
plt.rcParams.update({'font.size': 18}) # update font size
fig.savefig('3b.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot


##############################################################################
#   Ex. 4: Mixed best-response functions in a "(p,q)-diagram                 #
##############################################################################
# Ex. 4.b
fig, ax = plt.subplots(figsize=(6,6)) # create new figure
plt.plot([0,1/10,1/10,1], [0,0,1,1], 'r', label="$BR_1(q)$") # plotting the line 1 points
plt.plot([0,0,1,1], [0,9/10,9/10,1], 'b', ls='dashed', label="$BR_2(p)$") # plotting the line 2 points
plt.plot([0,1/10,1], [0,9/10,1], 'kX', markersize=18, label="$NE$") # plotting the PSNE points
plt.xlabel('q (probability of L)', color='b') # naming the x axis
plt.ylabel('p (probability of T)', color='r') # naming the y axis
plt.legend(bbox_to_anchor=(0, 1.02, 1, 1), # bbox=(x, y, width, height)
           loc='lower left', ncol=3, mode="expand", borderaxespad=0.)
plt.rcParams.update({'font.size': 18}) # update font size
fig.savefig('4b.pdf', bbox_inches='tight') # save the full plot to working folder
plt.show() # show the full plot

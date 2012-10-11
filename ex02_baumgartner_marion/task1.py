""" task2.py Exercise1
   TASK: gnerate a square lattice of arbitrary size NxN (here a 100x100 lattice was used) to study percolation
"""

__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 28/09/2012 $"

import random as rand
import pylab as pyl
import numpy as np



"""
functin generates a latixe
@param nx length of the lattice; int value
@param ny height of the lattice; int value
@param p probability which determines the cell is empty or occupied

@return xl a list of lists filled with 0 and 1. Every entry in the list is either empty (0) or occupied (1) 
"""
def initLattice(nx, ny, p):
    xL=list()
    for x in range(nx):
        yL=list()
        for y in range(ny):
            z=rand.random()
            if(z<p):
                yL.append(1) #occupied
            else:
                yL.append(0) #unoccupied
        xL.append(yL)
    return xL




 
fig=pyl.figure(1)

a1=fig.add_subplot(2,2,1)
p=0.3
#input paramete 1 the image 2 the interpolation to get neat squares 3 the colormap (default is blue red)
pyl.imshow(initLattice(100,100,p), interpolation='nearest')#,cmap=pyl.cm.gray)
pyl.title("p=%01.02f" % (p))

a2=fig.add_subplot(2,2,2)
p=0.592 #critical
pyl.imshow(initLattice(100,100,p), interpolation='nearest')
pyl.title("p=%01.03f" % (p))

a3=fig.add_subplot(2,2,3)
p=0.7
pyl.imshow(initLattice(100,100,p), interpolation='nearest')
pyl.title("p=%01.02f" % (p))

a4=fig.add_subplot(2,2,4)
p=0.9
pyl.imshow(initLattice(100,100,p), interpolation='nearest')
pyl.title("p=%01.02f" % (p))


pyl.setp(a1.get_xticklabels(), visible=False)
pyl.setp(a2.get_xticklabels(), visible=False)
pyl.setp(a2.get_xticklabels(), visible=False)
pyl.setp(a3.get_xticklabels(), visible=False)
pyl.setp(a4.get_xticklabels(), visible=False)
pyl.setp(a4.get_yticklabels(), visible=False)
pyl.setp(a1.get_yticklabels(), visible=False)
pyl.setp(a2.get_yticklabels(), visible=False)
pyl.setp(a3.get_yticklabels(), visible=False)

pyl.show()

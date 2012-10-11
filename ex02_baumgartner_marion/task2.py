""" task2.py Exercise1
   TASK: gnerate a square lattice of arbitrary size NxN (here a 100x100 lattice was used) to study percolation
"""

__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 28/09/2012 $"


import random as rand
import pylab as pyl
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

"""
functin generates a latixe
@param nx length of the lattice; int value
@param ny height of the lattice; int value
@param p probability which determines the cell is empty or occupied

@return xl a list of lists filled with 0 and 1. Every entry in the list is either empty (0) or occupied (1)

The lattice generated has a border of -1 on the top, bottom and left right sides in order to indicate that the "forest" ends there
"""

def initLattice(N, p, seed=0):
    xL=list()
    for x in range(N+2):
        yL=list()
        for y in range(N+2):
            z=rand.random()
            if(y==0 or y==N+1):
                yL.append(-1)
            elif(x==0 or x==N+1):
                yL.append(-1)
            elif(z<p):
                yL.append(1) #occupied
            else:
                yL.append(0) #unoccupied
        xL.append(yL)
    return xL


def burn(xinit,name,sFig=False):
    fig=pyl.figure(1)
    stepps=2
    pathLen=0
    
    #defining the color map for the graph
    #cmap = mpl.colors.ListedColormap(['white','cyan','green', 'red'])
    #bounds=[-1.5,-0.5,0.5,1.5,2.5]
    #norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    
    #setting the firs row to burning
    for i in range(1,len(xinit[0])-1):
        xinit[1][i]=stepps #2: tree is burning

    #plot the lattice
    #pyl.imshow(xinit, interpolation='nearest',cmap=cmap, norm=norm)
    #pyl.title("Initial Lattice (first row burning)")
    #pyl.savefig('%sInit.png'%(name))
    #pyl.show()
    
    # itterate (burne the forest in time stepps)
    while(True):
        stepps+=1 #one time step was made
        updates=0
        for x in range(1,len(xinit)-1):
            for y in range(1,len(xinit[x])-1):
                if(xinit[x][y]==stepps-1):
                    xinit[x][y]==3 #the tree is burned
                    if(xinit[x+1][y]==-1 and pathLen==0):#we reached the other end
                        pathLen=stepps-1
                    if(xinit[x+1][y]==1):
                        updates+=1
                        xinit[x+1][y]=stepps
                        
                    if(xinit[x][y+1]==1):
                        updates+=1
                        xinit[x][y+1]=stepps
                        
                    if(xinit[x-1][y]==1):
                        updates+=1
                        xinit[x-1][y]=stepps
                        
                    if(xinit[x][y-1]==1):
                        updates+=1
                        xinit[x][y-1]=stepps
        if(updates==0):#there is no more tree to be put on fire
            break
    
    #plot the final lattice
    #a2=fig.add_subplot(2,1,2)
    if(sFig):
        #define new colormap where burned trees are marked black
        cmap = mpl.colors.ListedColormap(['white','cyan','green','black','red'])
        bounds=[-1.5,-0.5,0.5,1.5,stepps-1.5, stepps]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        pyl.imshow(xinit, interpolation='nearest',cmap=cmap, norm=norm)
        pyl.title("Final lattice (after %d stepps; shortest path takes %d stepps)" %(stepps-1, pathLen))
        pyl.savefig('%sFin.png'%(name))
    #pyl.show()
    return [pathLen , stepps-1]
        
        
        
#critical
p=0.53
prob=[]
res1=[]
res2=[]
res3=[]
for i in range(10):
    p+=0.01
    save=False
    stat=[]
    for i in range(15):
        stat.append(burn(initLattice(25,p),'bla',save))
    prClus=0
    asp=0
    tof=0
    for i in range(len(stat)):
        if(stat[i][0]!=0):    
            prClus+=1
            asp+=stat[i][0]
        tof+=stat[i][1]
        
        
    prob.append(p)
    res1.append(prClus/float(len(stat)))
    res3.append(tof/float(len(stat)))
    if(prClus!=0):
        res2.append(asp/float(prClus))
    else:
        res2.append(asp)

fig=pyl.figure(1)
a1=fig.add_subplot(3,1,1)
pyl.plot(prob,res1,'bo')
a2=fig.add_subplot(3,1,2)
pyl.plot(prob,res2,'bo')
a3=fig.add_subplot(3,1,3)
pyl.plot(prob,res3,'bo')
pyl.xlabel("p")
a1.set_ylabel("percolative cluster")
a2.set_ylabel("avg. shortest path")
a3.set_ylabel("avg. time of fire")
pyl.show()
    
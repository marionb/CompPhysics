"""
    lattice.py
    
    Class to generate NxN lattice where cels with 1 are occupied. Cells with 0 are empty.
    
    Tree types of lattices can be genetrated:
        ->  lattic gan be generatet as a normal latice
        ->  with a border on all four sides (identified with -1)
        ->  bith periodic boundaries
    
    Class also has a function which plots the lattice usig a deafult or other color map. The image is safed with the given name
"""

__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 28/09/2012 $"


import random as rand
import pylab as pyl
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class Lattice:
    st=0
    N=0
    p=0
    seed=0
    xL=list()
    def __init__(self, lattSize=100, prob=0.59, s=0):
        self.N=lattSize
        self.p=prob
        self.seed=s
        
    def initLattice(self):
        for x in range(self.N):
            yL=list()
            for y in range(self.N):
                z=rand.random()
                if(z<self.p):
                    yL.append(1) #occupied
                else:
                    yL.append(0) #unoccupied
            self.xL.append(yL)
            
            
    def initBorderLattice(self):
        self.xL=list()
        for x in range(self.N+2):
            yL=list()
            for y in range(self.N+2):
                
                if(y==0 or y==self.N+1):
                    yL.append(-1)
                elif(x==0 or x==self.N+1):
                    yL.append(-1)
                else:#if not border fill according to p
                    z=rand.random()
                    if(z<self.p):
                        yL.append(1) #occupied
                    else:
                        yL.append(0) #unoccupied
            self.xL.append(yL)
            
    def initPeriodicLattice(self):
        #initiate a periodic lattica
        pass
    
        
    def printLattice(self):
        for i in range(len(self.xL)):
            print self.xL[i]
            
    #use a BorderLattice with this function        
    def determinePercCluster(self):
        stepps=2
        pathLen=0
        clustSize=0
        self.initBorderLattice()#create a new lattice with border
        for z in range(1,len(self.xL)):
            self.xL[z][1]=2 #start burning point in the first row and continue from there
            
            # itterate (burne the forest in time stepps)
            while(True):
                stepps+=1 #one time step was made
                updates=0
                for x in range(1,len(self.xL)-1):
                    for y in range(1,len(self.xL[x])-1):
                        if(self.xL[x][y]==stepps-1):
                            self.xL[x][y]==3 #the tree is burned
                            if(self.xL[x+1][y]==-1 and pathLen==0):#we reached the other end now we can deterine the shorst path with the amunt of stepps we took
                                pathLen=stepps-1
#                                print "the end has been reached the first time"
#                                print pathLen
                            if(self.xL[x+1][y]==1):
                                updates+=1
                                self.xL[x+1][y]=stepps
                                
                            if(self.xL[x][y+1]==1):
                                updates+=1
                                self.xL[x][y+1]=stepps
                                
                            if(self.xL[x-1][y]==1):
                                updates+=1
                                self.xL[x-1][y]=stepps
                                
                            if(self.xL[x][y-1]==1):
                                updates+=1
                                self.xL[x][y-1]=stepps
                clustSize+=updates #this gives the size of the current cluster
                if(updates==0):#there is no more tree to be put on fire
                    break
            if(pathLen!=0):
                break #we found a percolation cluster and we can stop
                #define new colormap where burned trees are marked black
        return [pathLen , stepps-1, clustSize]
    
    
    def plotLattice(self, stepps ,title="", name="test"):
        #define new colormap where burned trees are marked black
        cmap = mpl.colors.ListedColormap(['white','cyan','green','black'])
        bounds=[-1.5,-0.5,0.5,1.5,stepps]#<- warning is generated here!!!
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        pyl.imshow(self.xL, interpolation='nearest',cmap=cmap, norm=norm)
        pyl.title(title)
        pyl.savefig('%s.png'%(name))
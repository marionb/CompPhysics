"""
    clusterSize.py
    
    Task:
        Implement the Hoshen-Kopelman algorithem for  square lattice of size NxN probability p
    
"""

__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 28/09/2012 $"

import random as rand
import pylab as pyl
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import lattice as lt


def HoshenKopelman(lattice):
    k=0
    m_k=list()

    for x in range(len(lattice)):
        for y in range(len(lattice[x])):
            #print lattice
            if(lattice[x][y]==1):
                up=0 if x==0 else lattice[x-1][y]
                left=0 if y==0 else lattice[x][y-1]
                #print left
                #print up
                #print m_k
                if(up==0 and left==0):
                    lattice[x][y]=k
                    m_k.append(1)
                    k+=1
                else:
                    add=0
                    if((left!=0 and up==0) or (left!=0 and up!=0 and left==up)):
                        lattice[x][y]=left
                        m_k[left]+=1
                    elif(left==0 and up!=0):
                        lattice[x][y]=up
                        m_k[up]+=1
                    else: #(if left!=0 and up!=0)--> it gets a bit more complicated ;)
                        k_new=left if left>up else up
                        k_old=(left+up)-k_new
                        m_k[k_new]+=m_k[k_old]+1
                        m_k[k_old]-=k_new
                        lattice[x][y]=k_new
    d = {}
    for i in set(m_k):
        if(m_k.index(i)>0):
            d[i] = m_k.count(i)
            
    return [lattice, d]
                        
                        
                        
grid=lt.Lattice(10)
grid.initLattice()
tau=HoshenKopelman(grid.xL)
grid.xL=tau[0]
print tau[1]

grid.printLattice()

#cmap=mpl.colors.ListedColormap(['Navy','cyan','green'])
#bounds=[-1.5,-0.5,0.5,1.5]
grid.plotLattice("test","test im",  "accent")





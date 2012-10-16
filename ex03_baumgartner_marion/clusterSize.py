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
import matplotlib.mlab as mlab
import lattice as lt


def HoshenKopelman(lattice):
    k=2
    m_k=list()
    m_k.append(False)#m_k[0]=f
    m_k.append(False)#m_k[1]=f ->this is so that we can start at k=2!
    for x in range(len(lattice)):
        for y in range(len(lattice[x])):
            #print lattice
            if(lattice[x][y]==1):
                up=0 if x==0 else lattice[x-1][y]
                left=0 if y==0 else lattice[x][y-1]
                #print left
                #print up
                #print m_k
                if(up==0 and left==0):#create a new cluster
                    lattice[x][y]=k
                    m_k.append(1)
                    k+=1
                else:
                    add=0
                    if((left!=0 and up==0) or (left!=0 and up!=0 and left==up)):#if left belonges to a cluster or if left and up belonge to the same cluster
                        lattice[x][y]=left
                        m_k[left]+=1
                    elif(left==0 and up!=0):#if only up belinges to an exising cluster
                        lattice[x][y]=up
                        m_k[up]+=1
                    else: #(if left!=0 and up!=0) and left!=up--> it gets a bit more complicated ;)
                        k_new=left if left<up else up
                        k_old=(left+up)-k_new
                        #print "k_old; left ; up"
                        #print k_old, left, up   
                        m_k[k_new]+=m_k[k_old]+1
                        m_k[k_old]-=k_new
                        
                        lattice[x][y]=k_new
                
    #print m_k
    num=list()
    for i in range(2,len(m_k)):
        if(m_k[i]>0):
            #print "m_k[i] is:"
            #print m_k[i]
            num.append(m_k[i])
    
    
    #d = {}        
    #for i in set(num):
    #    d[i] = m_k.count(i)
    return [lattice, num]
                        
                        
                        
p=0.55
grid=lt.Lattice(500,p)
grid.initLattice()
tau=HoshenKopelman(grid.xL)


n, bins, patches=plt.hist(tau[1],50,range=None, normed=True, weights=None,
       cumulative=False, bottom=None, histtype='bar', align='mid',
       orientation='vertical', rwidth=None, log=False,
       color=None, label=None,)

plt.savefig("%s.png"%(p))
plt.show()






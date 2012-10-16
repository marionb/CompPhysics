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
    #CALCULATION THE CLUSTER SIZE DISTRIBUTION
    summe=0 
    n_s = []
    s=[]
    for i in set(num):
        n_s.append(m_k.count(i))
        s.append(i)
        summe+=m_k.count(i)
        
    for k in range(len(n_s)):
        n_s[k]=n_s[k]/float(summe)
    
    return [n_s, s, num, lattice]
                        
                        
                        
p=0.8 #CHANGE TO GET AN OTHER PROBABILITY
grid1=lt.Lattice(500,p)
grid1.initLattice()
tau=HoshenKopelman(grid1.xL)


plt.semilogy(tau[1],tau[0],'bo')
plt.xlabel("s")
plt.ylabel("log(n_s)")

plt.savefig("%s.png"%(p))






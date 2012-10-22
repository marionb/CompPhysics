"""
    task1.py
    
    Task:
        
    
"""

__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 19/10/2012 $"

import lattice as lt
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

size=100
ended=0
grid=lt.Lattice(size,0.592)

#finding a cluster with has percolation
while(ended==0):
    tau=grid.determinePercCluster()
    ended=tau[0]

print tau
grid.printLattice()

def sandBox(grid):
    #find center of grid -> grid hass to be a square else it will not work!
    x_mid=len(grid)/2

    #M(R) keeps the occupation in the box of width R    
    m=list()
    m.append(list())
    m.append(list())
    count=1
    if(grid[x_mid][x_mid]==0):
        return 0
    
    for r in range(1,x_mid):
        
        for x in range(x_mid-r, x_mid+r+1):
            for y in range(x_mid-r,x_mid+r+1):
                if(grid[x][y]>=2):
                    count+=1
        m[0].append(count)
        m[1].append(2*r+1)
    return m

print "sandbox result"
tau_sb=sandBox(grid.xL)
print tau_sb
x=np.log(tau_sb[0])
y=np.log(tau_sb[1])
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print "Gradient and intercept", slope, intercept
plt.plot(x, intercept + slope*x, 'r-')
plt.loglog(tau_sb[0], tau_sb[1],'bo')
plt.xlabel("log(R)")
plt.ylabel("log(M(R))")
plt.savefig("test.png")
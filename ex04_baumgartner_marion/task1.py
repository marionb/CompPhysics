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

size=50
ended=0
grid=lt.Lattice(size,0.592)

#finding a cluster with has percolation
while(ended==0):
    tau=grid.determinePercCluster()
    ended=tau[0]

#print "latice information"
#print tau
#grid.printLattice()

def sandBox(grid):
    
    if(type(grid)!=list):
        print"the value given is not a matrix"
        return 0
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
if(tau_sb!=0):
    grid.plotLattice(tau[1],"","lattice50") #this gives a warning because he does not like nonelinear color scales but it does the job (a bit ugly but oh well)
    print "sndbox tau"
    print tau_sb
    x=np.log(tau_sb[0])
    y=np.log(tau_sb[1])
    #print x
    #print y
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    
    print "Gradient and intercept", slope, intercept
    #plt.plot(x,y,'g+')
    #plt.plot(x, intercept + slope*x, 'r-')
    plt.loglog(tau_sb[0], tau_sb[1],'bo', label=b'calculated Data')
    plt.loglog(np.exp(x),np.exp(slope*x+intercept),'r-',label=r'$y=%g + %g x$'%(intercept, slope))
    plt.xlabel("$\log(R)$")
    plt.ylabel("$\log(M(R))$")
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.savefig("size50.png")
else:
    print "this progtam failed try again!!"
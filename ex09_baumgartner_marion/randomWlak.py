"""
    randomWalk.py
    
    Task:   Simple Random Walk
 
"""
__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 16/11/201$"
 
import numpy as np 
import random as rand
import matplotlib as mpl
from cmath import rect
import matplotlib.pyplot as plt
 
#global variable
T=10000


def RW(N,radius):
    """
    Generates a random walk starting at the origin (0,0)
    @ param N   the amount of steps done in the random walk.
    @ param r   size of the step; set to one by default
    @ return    an array containig the possition after every stepp, in a two dimensional x-y plane represented with complex numbed.
    """
    rand.seed()
    
    #initial position is choosen randomly
    r=np.sqrt(rand.random()) #
    psi=rand.random()*2.0*np.pi;
    p0=complex(radius*r*np.cos(psi),radius*r*np.sin(psi))
    walk=[p0]
    
    for i in range(N-1):#take 49 steps
        r=np.sqrt(rand.random()) #
        psi=rand.random()*2.0*np.pi;
        p0+=complex(radius*r*np.cos(psi),radius*r*np.sin(psi))
        walk.append(p0)
    
    distance=abs(walk[0]-walk[len(walk)-1])

    return walk, distance

def printWalk(path):
    x=list()
    y=list()
    for num in path:
        x.append(num.real)
        y.append(num.imag)
    plt.plot(x,y)
    plt.show()



def endPts(T,N=10,stepSize=1):
    """
    Fuction generates T randome walks an and adds the distance of the walk in an array.
    @param N        the amount of steps taken
    @param T        the amount of RW done
    @param stepSize the size of one step taken by the random walker
    """
    error1=0
    walkedDist=0
    for i in range(T):
        path, dist=RW(N,stepSize)
        walkedDist+=dist**2
        error1+=dist**4
        
    error1=error1/float(T)
    R2=1/float(T)*walkedDist
    error=np.sqrt(1/float(T)*(error1-R2**2))
    #print error
    return R2, error1/R2

N=range(2,100)
R2=[]
error=[]
rel=[]
for i in N:
    dis, err=endPts(i)
    R2.append(dis)
    error.append(err)
    #rel.append(err/dis)
#print "errors are", R2
#plt.subplot(111, yscale="log")
fig1=plt.figure()
ax=fig1.add_subplot(2,1,1) 
ax.plot(N, R2,'ro')
ay=fig1.add_subplot(2,1,2)
ay.plot(N,error)
print error


plt.show()
    
 
def plotStat(T):
    """
    Plot the Statistics for T random walks od the x distance the y distance and the total distance in histograms.
    """
    xd=arange(0,50,1)
    xxy=arange(-25,25,1)
    foo=linspace(0,500,5000)
 
    pdist, px, py=endPts(T)
    print px
    #hist(px, 100, 50, normed=1, facecolor='g', alpha=0.75)
    subplot(4,1,1)
    hist(px, xxy, normed=1, facecolor='g', histtype='step')
    subplot(4,1,2)
    hist(py,xxy, normed=1, facecolor='g', histtype='step')
    subplot(4,1,3)
    hist(pdist,xd, normed=1, facecolor='g', histtype='step')
 
    xlabel(r"distances", fontsize = 12)
    ylabel(r"probability", fontsize = 12)
    subplot(4,1,4)
    plot(foo, map(lambda x: Gaus(x,T), foo))    
    show()
 
def Gaus(r,N):
    """
    plot the gausian function
    """
    return 2*r/N*exp(-r*r/N)
 
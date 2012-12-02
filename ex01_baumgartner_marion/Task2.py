"""Task2.py Exercise 1
    TASK:       Generate homogeneous distribution of random (of perhaps moer like pseudo-random) numbes inside a circle
    
    SOLUTION:   The method used here uses a random angle psi [0, 2*pi] and a random radius r [0;radius] within a given radius. Then the coordinates are converted from
                polar in to cartesian coordinates.
                This method is probably not the fastest, as it uses sqrt, sin and cos. To improve this one could just find random points (x,y)
                within a square and then check werther they are also inside a circle within the square. If this is true keep the point if not
                generate a new one.
"""
__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 28/09/2012 $"



import numpy as np
import pylab as py
from math import cos, sin, pi, sqrt
import matplotlib.pyplot as plt
import random as rand



x=[0]
y=[0]
def fun(n):
    radius=2 #radius of the circle
    for i in range(0, n):
        r=sqrt(rand.random())
        psi=rand.random()*2.0*pi;
        x.append(radius*r*cos(psi))
        y.append(radius*r*sin(psi))
        
     
n=500 #amount of random point to be calculated within the circle   
fun(n)
plt.plot(x,y,'c*')
plt.show()

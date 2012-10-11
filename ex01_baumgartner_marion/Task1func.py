""" Task1.py Exercise1
   TASK: generate random numbes usin a congruential RNG
         1)Checking for correlations
         2)Creating a 3D plot
         3)Different RNG -> using the built in RNG and different c and p
   
   This file only containes the functions which are after used to generate the plots.
   FUNCTIONS:
         description od each function is given above the function
"""
__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 28/09/2012 $"



import numpy as np
import pylab as py
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random as rand

"""
   congruential RNG:
      calculates a number using the seed x0 as well as given c and p
"""
def RandNum(x0, c, p):
   xi=((c*x0)%p)
   return xi


"""
   Create a set of random numbers using RandNum and prepare them so that thei can be ploted on a 3D or 2D plot
"""
def createNum(p,c,n,seed=1.0):
   nums=[seed]
   numsx=[0.0]
   numsy=[0.0]
   numsz=[0.0,0.0]
   for i in range(0,n):
        nums.append(RandNum(nums[i],c,p))
        numsx.append(nums[i]/p)
   for i in range(0,n):
        numsy.append(numsx[i])
        numsz.append(numsx[i])
   numsz.pop(n) #remove extra number at the end
   return [numsx,numsy,numsz]
   
"""
   generate a set of random numbers using a pre-programed RND
"""
def initRand(n):
    numsx=[0.0]
    numsy=[0.0]
    numsz=[0.0,0.0]
    for i in range(0,n):
        numsx.append(rand.random())
    for i in range(0,n):
        numsy.append(numsx[i])
        numsz.append(numsx[i])
    numsz.pop(n) #remove extra number at the end
    return [numsx,numsy,numsz]
    
"""
   Mixing of 2d and 3d subplots:
      creating a 2D and a 3D plot with the given title.
      The 2D plot takes x and y to plot. the 3D plot plots x, y and z(x, y values are the same as in the 2D plot).
"""
def plot(title, x,y,z):
   fig = plt.figure(figsize=plt.figaspect(1.))
   fig.suptitle(title)
   ax = fig.add_subplot(2, 1, 1)
   l = ax.plot(x,y, 'bo', markerfacecolor='green')
   ax.grid(True)
   ax.set_xlabel('x_i')
   ax.set_ylabel('x_{i+1}')

   ax = fig.add_subplot(2, 1, 2, projection='3d')

   xLabel = ax.set_xlabel('x_i')
   yLabel = ax.set_ylabel('x_{i+1}')
   zLabel = ax.set_zlabel('x_{i+2}')
   ax.scatter(xs=x, ys=y, zs=z)
   


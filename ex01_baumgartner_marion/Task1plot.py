""" Task1.py Exercise1
        
    To have a look at the plots pleas run this file :)
    
    IMPORTANT: this file needs Task1func.py to run!
    
    TASK: generate random numbes usin a congruential RNG
         1)Checking for correlations
         2)Creating a 3D plot
         3)Different RNG -> using the built in RNG and different c and p
   
    OUTPUT
         1) 2D graph of random numbes (normalized)
         2) 3D graph of random numbes (normalized)
         This is plotet for different RNG
"""
__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 28/09/2012 $"



import numpy as np
import pylab as py
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random as rand 
import Task1func as T1



   
rn=T1.createNum(31,3,30)
#==>max number of planes p^{1/n}=
T1.plot('Square and Cube Test for RNG (using p=31, c=3)',rn[0],rn[1], rn[2])

rn=T1.createNum(17,3,30)
#==>max number of planes p^{1/n}=
T1.plot('Square and Cube Test for RNG (using p=17, c=3)',rn[0],rn[1], rn[2])
   
rn=T1.initRand(100)
T1.plot('Suare and Cube Test Using the RNG from the Random Librari',rn[0],rn[1], rn[2])

plt.show()
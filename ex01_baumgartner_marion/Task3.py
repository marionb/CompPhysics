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
import Task1func as T1

def countMeasure(arr):
    count=[0]*10
    for i in range(len(arr)):
        temp=arr[i]
        if(0<=temp<0.1):
            count[0]+=1
        elif(0.1<=temp<0.2):
            count[1]+=1
        elif(0.2<=temp<0.3):
            count[2]+=1
        elif(0.3<=temp<0.4):
            count[3]+=1
        elif(0.4<=temp<0.5):
            count[4]+=1
        elif(0.5<=temp<0.6):
            count[5]+=1
        elif(0.6<=temp<0.7):
            count[6]+=1
        elif(0.7<=temp<0.8):
            count[7]+=1
        elif(0.8<=temp<0.9):
            count[8]+=1
        elif(0.9<=temp<1.0):
            count[9]+=1
    return count

def chiSQR(count, n ,k):
    assert(k!=0)
    p=1/float(k)
    chi=0
    for i in range(1,k+1):
        chi+=(count[i-1]-n*p)**2/(n*p)
    print "chi^2="
    print chi
    return chi
    


rn1=T1.createNum(31,3,60)
N=countMeasure(rn1[0][1:len(rn1[0])-1])
chiSQR(N,50,10)

rn1=T1.createNum(31,3,60,0.21)
N=countMeasure(rn1[0][1:len(rn1[0])-1])
chiSQR(N,50,10)

rn1=T1.createNum(31,3,60,3.7)
N=countMeasure(rn1[0][1:len(rn1[0])-1])
chiSQR(N,50,10)

rn2=T1.createNum(17,3,60)
N=countMeasure(rn2[0][1:len(rn2[0])-1])
chiSQR(N,50,10)

n=60
rn3=T1.initRand(n)
N=countMeasure(rn3[0][1:len(rn3[0])-1])
chiSQR(N,n,10)



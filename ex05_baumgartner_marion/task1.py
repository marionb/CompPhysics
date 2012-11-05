"""
    task1.py
    
    Task:
        
    
"""

__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 29/10/2012 $"

import random as rand
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

"""
Distance between two points p1 and p2
"""
def dij_particle(p1,p2):
    return sp.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)
    
    
"""
generate a list of particle positions (centre of the speres) which do not overlap
n is the amount of points in the box
R the radius of the spheres from which the center coorinate is safed in the list which the function returnes
"""
def particle_list(R_sphere,L_box,n):
    
    particles=list()
    #print "D of the sphere",2*R_sphere

    particles.append([0,0,0])
    while(len(particles)<n):
        
        #print particles
        #create a new paricle position
        pi=[rand.uniform(0,L_box),rand.uniform(0,L_box),rand.uniform(0,L_box)]
        #print pi
        dummy_count=0
        #check if particle is not overlaping with existing particles
        for i in range(len(particles)):
            #print "dictance b/w 2 particles", dij_particle(pi,particles[i])
            if(2*R_sphere>dij_particle(pi,particles[i])):
                pass
            else:
                dummy_count+=1
        if(dummy_count!=0): #only add the particle if it was not rejected meaning the dummy_count variable is no longer 0
            particles.append(pi)
    return particles

"""
calculate the mean distance of a given configutation of particles -> particles beeing a list containing the coorinates of the centres of the spheres
"""
def dij_mean(particle):
    d_mean=0
    n=len(particle)
    for i in range(len(particle)):
        di=particle[i]
        for j in range(i+1,len(particle)):
            dj=particle[j]
            d_mean+=dij_particle(dj,di)
    norm=2.0/(1.0*(n*(n-1.0))) #Normalisation factor: make shure it is not an int and therfore equal to 0
    return norm*d_mean

"""
calculate the mean of a list of values
"""
def mean_val(val_list):
    tot=sum(val_list)
    return 1/(1.0*len(val_list))*tot
    
"""
claulate d_mean for different configurations

@param M:   Amount of configurations;       int
@param R:   size of sphere radius;          float
@param L:   box length => L^3 = Box_Vol;    float
@param n:   amont of spheres in the boc;    int
"""
def summ_up(M, R, L=100, n=10):
    conf=list()
    for i in range(M):
        pconf=particle_list(R,L,n)
        conf.append(dij_mean(pconf))
    return mean_val(conf)

plt_data=list()
x_val=range(1,100)
Len=100
n=30
R=1
for i in x_val:
    plt_data.append(summ_up(i,R,Len, n))

 
plt.plot(x_val,plt_data,'*r')
plt.title("average distance between %d points; square size is %d"%(n, Len))
plt.xlabel("$M$")
plt.ylabel("number of configurations $<d_mean>$")
plt.grid(True)
plt.show()
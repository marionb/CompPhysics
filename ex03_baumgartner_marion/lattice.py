"""
    lattice.py
    
    Class to generate NxN lattice where cels with 1 are occupied. Cells with 0 are empty.
    
    Tree types of lattices can be genetrated:
        ->  lattic gan be generatet as a normal latice
        ->  with a border on all four sides (identified with -1)
        ->  bith periodic boundaries
    
    Class also has a function which plots the lattice usig a deafult or other color map. The image is safed with the given name
"""

__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 28/09/2012 $"


import random as rand
import pylab as pyl
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class Lattice:
    N=0
    p=0
    seed=0
    xL=list()
    def __init__(self, lattSize=100, prob=0.59, s=0):
        self.N=lattSize
        self.p=prob
        self.seed=s
        
    def initLattice(self):
        for x in range(self.N):
            yL=list()
            for y in range(self.N):
                z=rand.random()
                if(z<self.p):
                    yL.append(1) #occupied
                else:
                    yL.append(0) #unoccupied
            self.xL.append(yL)
            
            
    def initBorderLattice(self):
        for x in range(self.N+2):
            yL=list()
            for y in range(self.N+2):
                
                if(y==0 or y==self.N+1):
                    yL.append(-1)
                elif(x==0 or x==self.N+1):
                    yL.append(-1)
                else:#if not border fill according to p
                    z=rand.random()
                    if(z<self.p):
                        yL.append(1) #occupied
                    else:
                        yL.append(0) #unoccupied
            self.xL.append(yL)
            
    def initPeriodicLattice(self):
        #initiate a periodic lattica
        pass
    
        
    def printLattice(self):
        for i in range(len(self.xL)):
            print self.xL[i]

from os import sys
from numpy import *
import matplotlib as mp
import matplotlib.pyplot as plt
import pylab as p
import random as rnd
import mpl_toolkits.mplot3d.axes3d as p3



roh = array([0.5,0.5]) #position of charge
box = [0,1] #size of box: [ xmin=ymin, xmax = ymax ]
N = 21. #number of points along one axis
gridpnts, dx = linspace(box[0],box[1],N, endpoint=True, retstep=True)
epsilon = 10e-10#10e-10

def jacobi(roh_xy):
    """
    
    """
    L=N
    old_grid=zeros([L,L])
    steps=0
    delta=1
    while(delta>epsilon):
        steps+=1
        delta=0
        new_grid=zeros([L,L])#set new grid to 0
        for i,xi in enumerate(gridpnts):
          #  print "in foor loop xi"
            if(xi==0 or xi==1):
                continue#if xi==1 or 0 we are on the border meaning for phi =0 ->imply boundary conditions
            for j, yj in enumerate(gridpnts):
         #       print "in foor loop yj"
                if(yj==0 or yj==1):
                    continue
                
                new_grid[i][j]=1/4.0*(old_grid[i+1][j]+old_grid[i-1][j]+old_grid[i][j+1]+old_grid[i][j-1])+dx*dx/4.0*roh_xy[i][j]
                alpha=abs(new_grid[i][j]-old_grid[i][j])
                if(alpha>delta):
                    delta=alpha
        #            print delta

       # print "steps", steps
        old_grid=new_grid
        
    print 'Jacobi relaxation ran with %d steps' %steps
    
    #plot
    fig=p.figure()
    
    gx,gy=p.meshgrid(gridpnts,gridpnts)
    ax = p3.Axes3D(fig)
    ax.scatter3D(ravel(gy),ravel(gx),ravel(old_grid))
    ax.contour3D(gridpnts,gridpnts,old_grid)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$\psi(x,y)$')
    plt.savefig("JpotentialSP3.png")
    
    fig2=plt.figure()
    plt.subplot(2,1,1)
    plt.imshow(old_grid, origin="lower")
    plt.colorbar()
    plt.title('2D Contour of the Jacobi Relaxation')
    
    plt.subplot(2,1,2)
    px,py = gradient(old_grid)
    plt.quiver(gridpnts,gridpnts,px,py)
    plt.title('Gradient Field of the Jacobi Relaxation')
    plt.savefig("JcontourSP3.png")
    return old_grid
    
        
def gauss_seidel(roh_xy):
    """
    
    """
    L=N
    old_grid=zeros([L,L])
    steps=0
    delta=1
    while(delta>epsilon):
        steps+=1
        delta=0
        #new_grid=zeros([L,L])#set new grid to 0
        for i,xi in enumerate(gridpnts):
          #  print "in foor loop xi"
            if(xi==0 or xi==1):
                continue#if xi==1 or 0 we are on the border meaning for phi =0 ->imply boundary conditions
            for j, yj in enumerate(gridpnts):
         #       print "in foor loop yj"
                if(yj==0 or yj==1):
                    continue
                val=old_grid[i][j]
                old_grid[i][j]=1/4.0*(old_grid[i+1][j]+old_grid[i-1][j]+old_grid[i][j+1]+old_grid[i][j-1])+dx*dx/4.0*roh_xy[i][j]
                alpha=abs(old_grid[i][j]-val)
                if(alpha>delta):
                    delta=alpha
        
    print 'Gaus Seidel relaxation ran with %d steps' %steps
    
    #plot
    fig=p.figure()
    
    gx,gy=p.meshgrid(gridpnts,gridpnts)
    ax = p3.Axes3D(fig)
    ax.scatter3D(ravel(gy),ravel(gx),ravel(old_grid))
    ax.contour3D(gridpnts,gridpnts,old_grid)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$\psi(x,y)$')
    plt.savefig("GSpotentialSP3.png")
    
    fig2=plt.figure()
    plt.subplot(2,1,1)
    plt.imshow(old_grid, origin="lower")
    plt.colorbar()
    plt.title('2D Contour of the Gauss-Seidel Relaxation')
    
    plt.subplot(2,1,2)
    px,py = gradient(old_grid)
    plt.quiver(gridpnts,gridpnts,px,py)
    plt.title('Gradient Fields of the  Gauss-Seidel Relaxation')
    plt.savefig("GScontourSP3.png")
    return old_grid
    
def main():

    nx = floor(roh[0]/(box[1]/N))
    ny = floor(roh[1]/(box[1]/N))
   # print nx, ny
    field=zeros([N,N])
    #field[nx][ny] = 1./(dx*dx)
    field[nx+9][ny+9] = 1./(dx*dx)
    field[nx-9][ny-9] = 1./(dx*dx)
    field[nx-9][ny+9] = 1./(dx*dx)
    field[nx+9][ny-9] = 1./(dx*dx)
    #plot the initial field;
    initFig=p.figure()
    gx,gy=p.meshgrid(gridpnts,gridpnts)
    ax = p3.Axes3D(initFig)
    ax.scatter3D(ravel(gy),ravel(gx),ravel(field))
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$\psi(x,y)$')
    plt.savefig("ROHxySP3.png")
    
    
    
    jacobi(field)
    gauss_seidel(field)

    
main()
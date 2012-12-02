"""
    NewtonMethod.py
    
    TASK: For the F(x,y)=exp(-(x-x_0)**2-(y-y_0)**2); use the generalized Newton method (Newton-Rapson) to numericaly detemine the maximumof such a function
    
    Description:
        Problem as a solulution of a system of equations:
            1) nabla F(x,y)=f(x,y)
            2) x_{n+1}=x_n+ J^{-1}*f(x_n)
            3) J_{ij}(x)=del f_i(x)/del x_j
                ->for the analytical solution of J see the report!
"""

__author__ = "Marion Baumgartner (marion.baumgartner@uzh.ch)"
__date__ = "$Date: 17/11/2012 $"


import numpy as np
import numpy.linalg as mat
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt





class ExtremaMethod():
    """
        Class to calculate the extrema point of the function F(x,y)=exp(-(x-x_0)**2-(y-y_0)**2)
        The Extrema can either be calculated using Newton-Rapson method or the Seacant method
    """
    def __init__(self, x_0, y_0, initX, initY,h=5):
        """
            @param x_0      determine the constant x_0 in the function
            @param y_0      determine the constant y_0 in the function
            @param initX    stating point x
            @param initX    stating point Y
            @param h        maximum amount of steps the integration takes (it might take fewer)
        """
        self.x_0=x_0
        self.y_0=y_0
        self.x_init=initX
        self.y_init=initY
        self.step=h
    
    def sfunc(self,x,y):
        """
            calculate the function F(x,y)=exp(-(x-x_0)**2-(y-y_0)**2)
            @param x    x value
            @param y    y value
        """
        return np.exp(-(x-self.x_0)**2.0-(y-self.y_0)**2.0)
        
    def func(self,x_vec):
        """
            calculate the function F(x,y)=exp(-(x-x_0)**2-(y-y_0)**2)
            @param x_vec    list containint the x and y value
        """
        x=x_vec[0]
        y=x_vec[1]
        return np.exp(-(x-self.x_0)**2.0-(y-self.y_0)**2.0)
    
    def derFunc(self,x_vec):
        """
            calculate the derivative of the function F(x,y)=exp(-(x-x_0)**2-(y-y_0)**2)
            @param x_vec    list containint the x and y value
        """
        x=x_vec[0]
        y=x_vec[1]
        z=np.array([2*(self.x_0-x),2*(self.y_0-y)])
        return z*self.sfunc(x,y)
        
    def Newton(self, newton=True, eps=0.0000001):
        """
            calculate exrema point of the function given further up.
            @param newton   IF this variable is set to true the Newton-Rapson method is usede
                            ELSE the secant method is used
            @param eps      maximum required percision of the method
            
            NOTE:   not shure if I am doing something wrong here or by calculating the Jacobian.
                    I am geting the exact same result for both methods no matter what initial points I use .
                    => might be buggy
        """
        x_new=np.zeros(2)
        x_old=np.array([self.x_init,self.y_init])
        #eps=10.0**(-5)
        delta=10
        count=0
        if(newton):
            while(True):
                count+=1
                invJacobi=self.secJacobian(x_old)
                if(type(invJacobi)==type(0)):##check that the jacobian is not singular
                    return x_new.tolist()
                part2=np.dot(invJacobi,np.array(self.derFunc(x_old)))

                x_new[0]=x_old[0]-part2[0]
                x_new[1]=x_old[1]-part2[1]
                if(abs(x_new[0]-x_old[0])>abs(x_new[1]-x_old[1])):
                    delta=abs(x_new[0]-x_old[0])
                else:
                    delta=abs(x_new[1]-x_old[1])

                x_old[0]=x_new[0]
                x_old[1]=x_new[1]
                print "printing x",x_new
                if(count>=self.step or eps>=delta):
                    return x_new.tolist()
                
           
        else:
            while(True):
                count+=1
                invJacobi=self.secJacobian(x_old)
                if(type(invJacobi)==type(0)):##check that the jacobian is not singular
                    return x_new.tolist()
                part2=np.dot(invJacobi,np.array(self.derFunc(x_old)))
                
                x_new[0]=x_old[0]-part2[0]
                x_new[1]=x_old[1]-part2[1]
                
                if(abs(x_new[0]-x_old[0])>abs(x_new[1]-x_old[1])):
                    delta=abs(x_new[0]-x_old[0])
                else:
                    delta=abs(x_new[1]-x_old[1])
                    
                x_old[0]=x_new[0]
                x_old[1]=x_new[1]
                print "printing x", x_new
                if(count>=self.step or eps>=delta):
                    return x_new.tolist()
        
        
    def newtonJacobian(self,r):
        """
            calculate the Jacobian matrice for the Newton-Rapson method and returne it's inverse
            -> function throws an error if Jacobi matrx is defined well
            @param r    vector with x and y values (these values max not be 0)
        """
        #x_vec=np.array(r)
        x=r[0]
        y=r[1]
        jacobi=np.zeros([2,2], float)
        
        
        jacobi[0][0]=(4.0*(self.x_0-x)**2.0-2.0)*self.sfunc(x,y)
        jacobi[1][1]=(4.0*(self.y_0-y)**2.0-2.0)*self.sfunc(x,y)
        jacobi[1][0]=4.0*(self.x_0-x)*(self.y_0-y)*self.sfunc(x,y)
        jacobi[0][1]=jacobi[1][0]
        #print "newton jacobian is ",jacobi
        try:
            return mat.inv(jacobi)
        except:
            print "singular jacobi not invertable"
            return 0
        
    
    def secJacobian(self, r,eps=(10**(-16))):
        """
            calculate the Jacobian matrice for the Secant method and returne it's inverse
            -> function throws an error if Jacobi matrx is singular well
            @param r    vector with x and y values
            @param eps  precision used to calculate the matrix entries
        """
        jacobi=np.zeros([2,2], float)
        sqrt_eps=np.sqrt(eps)
        h_0=sqrt_eps*r[0]
        h_1=sqrt_eps*r[1]        
        e_0=np.array([1,0])
        e_1=np.array([0,1])
        x_vec=np.array(r)
        jacobi[0][0]= (self.derFunc(x_vec+h_0*e_0)[0]-self.derFunc(x_vec))[0]/h_0
        jacobi[1][1]= (self.derFunc(x_vec+h_1*e_1)[1]-self.derFunc(x_vec))[1]/h_1
        jacobi[1][0]= (self.derFunc(x_vec+h_0*e_0)[1]-self.derFunc(x_vec))[1]/h_0
        jacobi[0][1]= (self.derFunc(x_vec+h_1*e_1)[0]-self.derFunc(x_vec))[0]/h_1
        #print "secant jacobian is ",jacobi
        try:
            return mat.inv(jacobi)
        except:
            print "singular jacobi not invertable"
            return 0
        
    def printfunc(self):
        """
            plot the function given above and the exrema points found with both methods
        """
        zero1=self.Newton(True)
        print "Using initial porition %0.2f ,%0.2f" %(self.x_init,self.y_0)
        print "extremum calculated witn Newton-Rapson: %0.2f ,%0.2f."%(zero1[0],zero1[1])
        zero2=self.Newton(False)
        print "extremum calculated witn Secant: %0.2f ,%0.2f." %(zero2[0],zero2[1])
        xlist=np.arange(self.x_0-10,self.x_0+10,0.01)
        ylist=np.arange(self.y_0-10,self.y_0+10,0.01)
        X,Y=np.meshgrid(xlist,ylist)
        Z=self.sfunc(X,Y)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
       
        ax.plot(xlist, ylist, self.sfunc(xlist,ylist), 'g-',label='function $e^{(-(x-%0.2f)^2-(y-%0.2f)^2)}$' %(self.x_0,self.y_0))
        ax.contour(X, Y, Z)# colors = 'k', linestyles = 'solid')
        ax.plot([zero1[0]], [zero1[0]], self.sfunc(zero1[0],zero1[1]),'bo',label='extrema using Newton-Rapson (%0.2f; %0.2f)'%(zero1[0],zero1[1]))
        ax.plot([zero2[0]], [zero2[0]], self.sfunc(zero2[0],zero2[1]),'ro',label='extrema using Seacent (%0.2f; %0.2f)'%(zero2[0],zero2[1]))
        ax.legend()
        plt.show()
        


x_0=10.0
y_0=10.0
newton=ExtremaMethod(x_0,y_0,9.3,9.3)

newton.printfunc()

    

 




import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
class Euler:
    def __init__(self, v_0, alpha_0, time, gamma=1, x_init=0,y_init=0):
        """
        @param v_0      initial velocity
        @param alpha_0  initial angel
        @param time     size of the timesteps
        @param gamma=1  friction coefficient
        @param x_init   initial position (x-coorinate)
        @param y_init   initial position (y_coordinate)
        """
        self.v_init=np.array([v_0*np.cos(alpha_0),v_0*np.sin(alpha_0)])
        self.r_init=np.array([x_init,y_init])
        self.delta=time
        self.gamma=gamma
        self.g=9.81 #gravitational const in [m/s]
        self.v_old=[]
        self.v_new=[]
    
    def fun(self,v_vec):
        """
        @param v_vec  vector/list with v_x v_z gives the point at which the derivative "func" is calculaed
        """
        fx=-self.gamma*v_vec[0]
        fy=-self.g-self.gamma*v_vec[1]
        return np.array([fx,fy])
        
    def funcpos(self, ti):
        """
        @param ti  time at which the position is to be calculated
        """
        fpx=self.v_old[0]
        fpy=self.v_old[1]
        return np.array(fpx,fpy)
        
    def method(self,eps=0.0001):
        """
        @param eps  breakof contition; if change from one iteration to the next in v is smaller than eps
                    the itteration will stop.
        """
        
        time=0
        
        self.v_old=self.v_init
        self.v_new=self.v_old
        vallx=[]
        vally=[]

        x_new=self.r_init
        posx=[]
        posy=[]
        
        timestepps=[]
        
        while(True):
            
            #print x_new
            #print time
            vallx.append(self.v_new[0])
            vally.append(self.v_new[1])
            
            posx.append(x_new[0])
            posy.append(x_new[1])
            
            timestepps.append(time)
            self.v_new=self.v_old+self.delta*self.fun(self.v_old)
            x_new=self.v_new*time+self.r_init
            
            #breakoff condition
            time+=self.delta #advance one timestepp
            meanDiff=0.5*(self.v_old[0]-self.v_new[0]+self.v_old[1]-self.v_new[1])

            if(self.v_new[1]<-self.v_init[1] or x_new[1]<0):
                return self.v_new, [vallx,vally], [posx, posy], timestepps
            else:
                self.v_old=self.v_new
                

def main():
    delta=0.001
    #comparison of different initial angles at an initial velocity of 2
    fig1=plt.figure()
    v_init=2
    for alpha in np.linspace(np.pi/8,3*np.pi/8,6):
        
        #alpha=float(i)*np.pi/8.0
        obj=Euler(v_init,alpha,delta)
        
        vend,v,x ,time=obj.method()   
 
        plt.plot(x[0],x[1],label="$v_0=$%g, $\phi =$%g" %(v_init, alpha))
        lg=plt.legend(loc='upper right')
        lx = plt.xlabel("x position")
        ly = plt.ylabel("y position")
        
    plt.savefig("angle.png")
    
    #comparision of different initial velocitioes at an angler of pi/4
    fig2=plt.figure()
    alpha=np.pi/4.0
    for i in [1,2,3,4,5,6]:
        v_init=float(i)
        obj=Euler(v_init,alpha,delta)
        
        vend,v,x ,time=obj.method()   
 
        plt.plot(x[0],x[1],label="$v_0=$%g, $\phi =$%g" %(v_init, alpha))
        lg=plt.legend(loc='upper right')
        lx = plt.xlabel("x position")
        ly = plt.ylabel("y position")
        
    plt.savefig("vel.png")
    
    #comparison of differnt friction coefficients at an angle of 0.7068 and an initial velocity of 2
    fig3=plt.figure()
    alpha_max=np.linspace(np.pi/8,3*np.pi/8,6)[2]
    v_init=2
    
    for friction in np.linspace(0,9,10):
        v_init=float(i)
        obj=Euler(v_init,alpha,delta,friction)
        
        vend,v,x ,time=obj.method()   
 
        plt.plot(x[0],x[1],label="$\gamma =$%g" %(friction))
        lg=plt.legend(loc='upper right')
        lx = plt.xlabel("x position")
        ly = plt.ylabel("y position")
        
    plt.savefig("fric.png")
    
if __name__ == '__main__': main()
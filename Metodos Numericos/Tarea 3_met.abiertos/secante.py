import numpy as np

def f(x):
    #return np.sin(x) + np.cos(1+x**2) - 1
    return x**3-6*x**2+4*x-6.1

def metodo_secante(f,x0,x1,es,imax):
    
    iter = 0
    ea = 100
    
    while(ea > es and iter <= imax):
        fp = (f(x1) - f(x0))/(x1 - x0)
        
        x = x1 - f(x1)/fp
        if(x != 0):
            ea = abs((x - x1)/x)
        
        x0 = x1
        x1 = x
        
        iter += 1
        
        print(iter, x, ea)

metodo_secante(f,2.5,3.5,0.01,5)

import numpy as np

def f(x):
    return np.sin(np.sqrt(x))-x
    
def g(x):
    return np.sin(np.sqrt(x))
    
def punto_fijo(f,g,xi,es,imax):
    ea = 100
    i = 0
    
    while(ea > es and i <= imax):
        if(i > 0):
            ea = np.abs(g(xi)-xi)
        xi = g(xi)
        i += 1
        
        print(i, xi, ea)
        
punto_fijo(f,g,0.5,0.01,30)

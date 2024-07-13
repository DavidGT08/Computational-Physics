import numpy as np

def f(x):
    #return -25+82*x-90*x**2+44*x**3-8*x**4+0.7*x**5 
    #return 0.8*x-0.3
    return x**(3.5)-80
    #return (9.8*x/15)*(1-np.exp(135/x))-35

def Metodo_Falsa(f,xl,xu,es,imax):
    iter = 0
    fl = f(xl)
    fu = f(xu)
    ea = 0
    xr = 0
    il = 0
    while (ea < es or iter >= imax):
        xrold = xr
        xr = xu - fu * (xl - xu) / (fl - fu)
        fr = f(xr)
        iter = iter + 1
        if (xr < 0 or xr > 0):
            ea = abs((xr - xrold) / xr) * 100
            et = 0.375 - xr
        test = fl * fr
        if(test < 0):
            xu = xr
            fu = f(xu)
            iu = 0
            il = il + 1
            if (il >= 2):
                fl = fl / 2
            elif (test > 0):
                xl = xr
                fl = f(xl)
                il = 0
                iu = iu + 1
                if (iui >= 2):
                    fu = fu / 2
            else:
                ea = 0
        print("Iteracion",iter," Raiz:",xr," Error aprox:",ea," Error verdad:",et)
    Metodo_Falsa = xr
        

#Metodo_Falsa(f,0.5,1,0.2,100)
#Metodo_Falsa(f,1,3,0.2,3)
Metodo_Falsa(f,2,5,2.5,100)
#Metodo_Falsa(f,59,60,0.1,100)

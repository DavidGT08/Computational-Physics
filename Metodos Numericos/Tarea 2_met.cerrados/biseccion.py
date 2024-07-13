from math import *

def f(x):
    return -25+82*x-90*x**2+44*x**3-8*x**4+0.7*x**5

def Metodo_Biseccion(f,xl,xu,ea):

    m1 = xl
    m = xu
    iter = 0

    while(abs(m1-m)>ea):
        m1 = m
        m = (xl+xu)/2
        if(f(xl)*f(m)<0):
            xu = m
        if(f(m)*f(xu)<0):
            xl = m
        iter = iter + 1
        es = abs(m1-m)
        print("Iteracion",iter," Raiz:",m," Error aprox:",es)

Metodo_Biseccion(f,0,1,1e-6)

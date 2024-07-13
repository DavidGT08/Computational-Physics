import math

def f(x):
    return -20*math.exp(-0.2*x)+20*math.exp(-0.75*x)

def df(x):
    return 4*math.exp(-0.2*x)-15*math.exp(-0.75*x)

def newton_raphson(f,df,xi,es):
    x = xi
    ea = 100
    iter = 0

    while(ea > es):
        x = x - f(x)/df(x)
        ea = abs(f(x))
        iter += 1

        print(iter, x,ea)

newton_raphson(f,df,10,0.01)

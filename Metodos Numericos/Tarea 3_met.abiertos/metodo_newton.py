def f(x):
    return -0.9*x**2+1.7*x+2.5

def df(x):
    return -1.8*x+1.7

def newton_raphson(f,df,xi,tolerancia):
    x = xi
    error = 100
    n = 0

    while(error > tolerancia):
        x = x - f(x)/df(x)
        error = abs(f(x))
        n += 1

        print(f'Numero de iteracion: {n}, Raiz: {x}, Error: {error}')

newton_raphson(f,df,5,0.01)

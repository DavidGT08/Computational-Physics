import numpy as np

cadena1 = "Calculo de integral impropia\n".capitalize() 
print(cadena1.center(50, " ")) 

a = float(input("Ingrese el limite inferior de la integral: "))
b = float(input("Ingrese el limite superior de la integral: "))
n = int(input("Numero de iteraciones 'n': "))

def f(x):
    return (1/x*(x+2))
    #return (1/np.sqrt(2*np.pi)*np.exp(-x**2/2))
    #return (1/(1+x**2)*(1+x**2/2))
    #return (np.exp(-x)*np.sin(x)**2)
    #return (x*np.exp(-x))

def conversion(f,t):
    return (1/t**2*(f(1/t)))

def simpson(a,b,n,conversion):
    sum = 0
    int = 0
    h = (b-a)/n #delta

#regla de simpson1/3
    for i in range(n+1):
        x = (1/a + (i*h))
#casos
        if (x == a or x == b):
            sum += f
        elif (i % 2 != 0):
            f = 4*f
            sum += f
        elif (i % 2 == 0):
            f = 2*f
            sum += f
#resultado  
    int = sum*(h/3)
    print("El resultado de la integral es: ", int)

simpson(a,b,n)    
"""
Programa para calcular la extrapolacion de Richardson
"""
import numpy as np

cadena0 = "Derivadas numericas por Extrapolacion de Richardson\n".capitalize() 
print(cadena0.center(70, " "))

x = float(input("Ingrese el punto donde a evaluar 'x': "))
h1 = float(input("Ingrese el tamaño del paso 'h1': "))
h2 = float(input("Ingrese el tamaño del paso 'h2': "))

def f(x):
    return np.log(x)
    #return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

#formula de diferenciacion centrada O(h^2)
def deri_h1(x,h1):
    D2 = (f(x+h1) - f(x-h1)) / (2*h1)
    return D2
deri_h1(x,h1)

def deri_h2(x,h2):
    D2 = (f(x+h2) - f(x-h2)) / (2*h2)
    return D2
deri_h2(x,h2)


def richardson(x,h1,h2):
#formula de la extrapolacion de richardson
    DR = (4/3)*deri_h2(x,h2)-(1/3)*deri_h1(x,h1)
    print("\n\nLa derivada es: ",DR)

richardson(x,h1,h2)   

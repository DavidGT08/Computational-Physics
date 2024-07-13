""""
Programa para calcular la primera derivada numericas
"""
import math
import sympy as sp
from sympy import Symbol
from scipy.misc import derivative

cadena0 = "Derivadas numericas\n".capitalize() 
print(cadena0.center(50, " "))

x = float(input("Ingrese el punto a evaluar 'x': "))
h = float(input("Ingrese el tamaño de los pasos 'h': "))

def f(x):
    #return math.sin(x)
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

#Hacia delante
cadena1 = "\n\n Derivadas hacia delante\n".capitalize() 
print(cadena1.center(50, " ")) 

def deri_dO(x,h):
    D = (f(x+h) - f(x)) / (h)
    print("La primera derivada O(h) es: ",D)
    e_t = abs((math.sqrt(2)/2-D)/100)
    print("El error absoluto porcentual es: ",e_t,"%")

def deri_dO2(x,h):
    D = (-f(x+h*2) + 4*f(x+h) -3*f(x)) / (2*h)
    print("La primera derivada O(h^2) es: ", D)
    e_t = abs((math.sqrt(2)/2-D)/100)
    print("El error absoluto porcentual es: ",e_t,"%")
#invocar funciones
deri_dO(x,h)
deri_dO2(x,h)

#Hacia atras
cadena2 = "\n\n Derivadas hacia atras\n".capitalize() 
print(cadena2.center(50, " ")) 

def deri_aO(x,h):
    D = (f(x) - f(x-h)) / (h)
    print("La primera derivada O(h) es: ",D)
    e_t = abs((math.sqrt(2)/2-D)/100)
    print("El error absoluto porcentual es: ",e_t,"%")

def deri_aO2(x,h):
    D = (3*f(x) - 4*f(x-h) +f(x-h*2)) / (2*h)
    print("La primera derivada O(h^2) es: ", D)
    e_t = abs((math.sqrt(2)/2-D)/100)
    print("El error absoluto porcentual es: ",e_t,"%")
#invocar funciones
deri_aO(x,h)
deri_aO2(x,h)

#Centrada
cadena3 = "\n\n Derivadas centrada\n".capitalize() 
print(cadena3.center(50, " ")) 

def deri_cO2(x,h):
    D = (f(x+h) - f(x-h)) / (2*h)
    print("La primera derivada O(h^2) es: ",D)
    e_t = abs((math.sqrt(2)/2-D)/100)
    print("El error absoluto porcentual es: ",e_t,"%")

def deri_cO4(x,h):
    D = (-f(x+h*2) + 8*f(x+h) -8*f(x-h) + f(x-h*2)) / (12*h)
    print("La primera derivada O(h^4) es: ", D)
    e_t = abs((math.sqrt(2)/2-D)/100)
    print("El error absoluto porcentual es: ",e_t,"%")
#invocar funciones
deri_cO2(x,h)
deri_cO4(x,h)


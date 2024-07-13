"""
Programa para calcular método de Heun
"""

from math import *
import numpy as np

cadena0 = "Metodo de Heun\n".capitalize() 
print(cadena0.center(50, " "))

def f(t,y):
    func = t*exp(3*t)-2*y
    return func

def Heun(t,y,h,n):
    print('y(',t,')=',y)

    for k in range(n):
        y = y + h*f(t,y)
        t = t + h
        print('y(',t,')=',y)

Heun(0,2,0.25,4)
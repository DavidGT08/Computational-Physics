"""
Programa para calcular la derivada de datos irregularmente espaciados
"""
import numpy as np

cadena0 = "Derivada para datos irregularme espaciados\n".capitalize() 
print(cadena0.center(70, " "))

x = float(input("Ingrese el punto donde quiere evaluar 'x': "))

#arreglo con primeros 3 datos
x1 = [0,25,50]
y1 = [0,32,58]
#arreglo con segundos 3 datos
x2 = [75,100,125]
y2 = [78,92,100]

def derivada(x1,y1,x2,y2):
    D = y1[0]*(2*x-x1[1]-x1[2])/((x1[0]-x1[1])*(x1[0]-x1[2]))+y1[1]*(2*x-x1[0]-x1[2])/((x1[1]-x1[0])*(x1[1]-x1[2]))+y1[2]*(2*x-x1[0]-x1[1])/((x1[2]-x1[0])*(x1[2]-x1[1]))+y2[0]*(2*x-x2[1]-x2[2])/((x2[0]-x2[1])*(x2[0]-x2[2]))+y2[1]*(2*x-x2[0]-x2[2])/((x2[1]-x2[0])*(x2[1]-x2[2]))+y2[2]*(2*x-x2[0]-x2[1])/((x2[2]-x2[0])*(x2[2]-x2[1]))
    print("La derivada en",x,"es",D)
derivada(x1,y1,x2,y2)
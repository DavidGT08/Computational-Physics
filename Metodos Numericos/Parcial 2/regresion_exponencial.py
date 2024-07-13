import math
import numpy as np
import matplotlib.pyplot as plt

cadena = "Regresión lineal a datos exponenciales".capitalize() 
print(cadena.center(50, " ")) 

#arreglo con valores 
x=[0.5,1,1.5,2,2.5]
y=[0.541,0.398,0.232,0.106,0.052]
#x=[10,20,30,40,50,60,70,80]
#y=[25,70,380,550,610,1220,830,1450]

#numeros de datos
n = len(x)
#convertir en vectores
x = np.array(x)
y = np.array(y)

#sumatorias
sumx = sum(x)
sumy = sum(y)
sumx2 = sum(x**2)
sumy2 = sum(y**2)
sumxy = sum(x*y)

#promedio de datos
xm = sumx/n
ym = sumy/n
#valores de la recta
a1 = (sumx*sumy-n*sumxy)/((sumx)**2 - n*sumx2) #pendiente (m)
a0 = ym - a1*xm #interseccion con el eje (b)
#errores del metodo
st = sum((y - ym)**2)
sr = sum((y - a1*x - a0)**2)

syx = math.sqrt(sr/(n-2)) #error estand.
r = math.sqrt((st - sr)/st) #coef.correlacion
print("Error estandar: ", syx)
print("Coeficiente de correlacion: ", r)

print('Pendiente               Interseccion con el eje X')
print(f'{a1:10} ==> {a0:10f}')

#graficar
plt.plot(x,y, 'o', label='Datos',color='red') #puntos
#plt.plot(x, np.log(a0)+a1*x, label='-0.254x-0.6468',color='green') #recta 
plt.plot(x, -0.254*x+0.6468, label='-0.254x+0.6468',color='green') #recta 

#titulo de ejes
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()#generar malla
plt.title('Regresion lineal')#titulo de grafica
plt.legend()#mostrar recuadro
plt.show()#mostrar grafica

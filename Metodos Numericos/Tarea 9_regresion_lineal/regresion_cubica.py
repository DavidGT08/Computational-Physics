import math
import numpy as np
import matplotlib.pyplot as plt

#arreglo con valores 
x=[3,4,5,7,8,9,11,12]
y=[1.6,3.6,4.4,3.4,2.2,2.8,3.8,4.6]
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
r2 = (st - sr)/st #coef.correlacion
print("Error estandar: ", syx)
print("Coeficiente de determinacion: ", r2)

print('Pendiente               Interseccion con el eje X')
print(f'{a1:10} ==> {a0:10f}')

#graficar
plt.plot(np.log10(x),np.log10(y), 'o', label='Datos',color='red') #puntos
plt.plot(np.log10(x), a1*np.log10(x)+np.log10(a0), label='0.136x+2.291',color='green') #recta 
#titulo de ejes
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()#generar malla
plt.title('Regresion lineal')#titulo de grafica
plt.legend()#mostrar recuadro
plt.show()#mostrar grafica

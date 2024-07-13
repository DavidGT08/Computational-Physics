import numpy as np
import matplotlib.pyplot as plt
import math

#imprimir grafica de la derivada
x = np.array(range(10))*0.1
y = np.zeros(len(x))

for i in range(len(x)):
   y[i] = 6*x[i]/(1-3*(x[i])**2)**2
    
    # y[i] = math.sin(x[i])

plt.plot(x,y,color='r')

plt.xlabel('Eje x')
plt.ylabel('Eje y')

#plt.legend()
plt.grid()
plt.show()

#evaluar derivada

#pedir evaluacion
x = float(input("Ingrese el numero a evaluar: "))

#definir funcion
fun = 6*(x)/(1-3*(x)**2)**2

print("Para 3 digitos de corte ", round(fun,3)) #3 digitos de corte
print("Para 4 digitos de corte ", round(fun,4)) #4 digitos de corte 


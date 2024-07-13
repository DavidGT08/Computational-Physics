import numpy as np
import math


#inicializar la serie
serie = 0
serie1 = 0

real = (math.pi**4)/90


#bucle para hacer la sumatoria de 1-10,000
for x in np.arange(1, 10000,1):
    serie += (1/x**4)

ea = ((real-serie)/real)*100

print("\n" + "La aproximacion de 1-10,000 es: " + str(serie))

print("El error relativo porcentual es: " + str(ea) + "%" + "\n\n")

#bucle para hacer la sumatoria de 10,000-1
for x in np.arange(10000,1,-1):
   serie1 += (1/x**4)

ea1 = ((real-serie1)/real)*100

print("La aproximacion de 10,000-1 es:" + str(serie1))
print("El error relativo porcentual es:" + str(ea1))


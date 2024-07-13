import math

cadena = "Calculo del trabajo al estirar un arco\n".capitalize() 
print(cadena.center(50, " ")) 

#masa de la flecha (cte)
m = 0.075
#lista con datos del problema
F = [0,37,71,104,134,161,185,207,225,239,250]

def trabajo(F,m):
#regla del trapecio para datos irregularmente espaciados
    h = 0.05 #paso constante
    sum = 0
    for i in range(0,10):
        sum += F[i]+F[i+1]
        i = i-1
    W = (h/2) * sum
    print("El trabajo realizado es: ",W,"N")

#calculo de la velocidad
    vel = math.sqrt(2*W/m)
    print("La velocidad de la flecha es: ",vel,"m/s")

trabajo(F,m)

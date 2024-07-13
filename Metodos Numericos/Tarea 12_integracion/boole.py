import math

cadena = "Regla de Boole".capitalize() 
print(cadena.center(50, " ")) 

a = float(input("Ingrese el limite inferior de integracion: "))
b = float(input("Ingrese el limite superior de integracion: "))

def boole(a,b):
#funcion
    f = lambda x:1-x-4*x**3+2*x**5

#puntos medios
    m1 = (2*a+b)/4
    m2 = (a+2*b)/4
    m3 = a+b/2
#regla de boole
    integral = 2*(b-a)/45 * (7*f(a) + 32*f(m1)+ 12*f(m2) + 32*f(m3) + 7*f(b))

    error = abs((1104-integral)/100)
    print("El error relativo porcentual es:", error,"%\n")

    print("El resultado de la integral es: ", integral)

boole(a,b)


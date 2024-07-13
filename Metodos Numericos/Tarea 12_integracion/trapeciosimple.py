import math    

#declarar la funcion
f = lambda  x:(1-x-4*x**3+2*x**5)

#inicializar el contador i y la suma
i = 0
s = 0

cadena = "Metodo del trapecio".capitalize() 
print(cadena.center(50, " ")) 

    #pedir al usuario "a"
a = float(input("Ingresa el limite inferior de la funcion: "))
    #pedir al usuario "b"
b = float(input("Ingresa el limite superior de la funcion: "))


def trapecio(a,b):
#calculo de delta x
    delta = (b-a)
    integral = delta*(f(a)+f(b))/2

    error = abs((1104-integral)/100)

#imprimir el resultado en pantalla

    print("El resultado de la integral es: ", integral)
    print("El error relativo porcentual es:", error,"%")

trapecio(a,b)


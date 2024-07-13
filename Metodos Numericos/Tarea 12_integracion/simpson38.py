import math

cadena = "Regla de Simpson 3/8".capitalize() 
print(cadena.center(50, " ")) 

a = float(input("Ingrese el limite inferior de integracion: "))
b = float(input("Ingrese el limite superior de integracion: "))
n = int(input("Numero de iteraciones 'n': "))

def simpson38(a,b,n):
#funcion
    #f = lambda x:(4*x-3)**3
    f = lambda x:1-x-4*x**3+2*x**5
    #f = lambda x:-3*x**6/1280 + 25*x**5/384 - 113*x**4/192 + 143*x**3/96 + 64*x**2/15 - 73*x/4 + 5
#delta
    h = (b-a)/n
#puntos medios
    m1 = (2*a+b)/3
    m2 = (a+2*b)/3
#regla de simpson
    integral = (b-a)/8 * (f(a) + 3*f(m1)+ 3*f(m2) + f(b))
    for i in range(n+1):
        sum = 0
        b = a+h
        area = integral
        sum += integral
        a = b

        error = abs((1104-integral)/100)
        print("El error relativo porcentual es:", error,"%\n")

    print("El resultado de la integral es: ", integral)

simpson38(a,b,n)  

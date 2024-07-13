import math

cadena = "Regla de Simpson 1/3".capitalize() 
print(cadena.center(50, " ")) 


a = float(input("Ingrese el limite inferior de integracion: "))
b = float(input("Ingrese el limite superior de integracion: "))
n = int(input("Numero de iteraciones 'n': "))

def simpson(a,b,n):
    sum = 0
    int = 0
    h = (b-a)/n #delta

#regla de simpson1/3
    for i in range(n+1):
        x = (a + (i*h))
#funcion
        #f = (4*x-3)**3
        f = 1-x-4*x**3+2*x**5
#casos
        if (x == a or x == b):
            sum += f
        elif (i % 2 != 0):
            f = 4*f
            sum += f
        elif (i % 2 == 0):
            f = 2*f
            sum += f
            
#resultado  
    int = sum*(h/3)

    print("El resultado de la integral es: ", int)

simpson(a,b,n)    



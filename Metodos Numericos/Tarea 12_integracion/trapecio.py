import math    

#declarar la funcion
#f = lambda  x:(1-x-4*x**3+2*x**5)
#f = lambda x:(4*x-3)**3
#f = lambda x:0.000107473544973545*x**7 - 0.00402447089947092*x**6 + 0.0603009259259261*x**5 - 0.46068121693122*x**4 + 1.8614169973545*x**3 - 3.6710085978836*x**2 + 3.21388888888889*x
f = lambda x:8.41187169312169e-5*x**7 - 0.00291889880952381*x**6 + 0.0398466435185185*x**5 - 0.270533234126984*x**4 + 0.945456142526455*x**3 - 1.56619072420635*x**2 + 0.954255952380952*x
#inicializar el contador i y la suma
i = 0
s = 0

cadena = "Metodo del trapecio".capitalize() 
print(cadena.center(50, " ")) 

    #pedir al usuario "a"
a = float(input("Ingresa el limite inferior de la funcion: "))
    #pedir al usuario "b"
b = float(input("Ingresa el limite superior de la funcion: "))

    #pedir al usuario "n"
n = int(input("Ingresa el numero de particiones 'n': "))

def trapecio(a,b,n):
#calculo de delta x
    delta = (b-a)/n
    sumatoria = (f(a)+f(b))/2
    
    #sumatoria del metodo usan un ciclo for
    for i in range(0,n+1):

        sumatoria += f(a + i*delta)

#calculo del metodo completo
        integral = delta * sumatoria
        
#imprimir el resultado en pantalla
    print("El resultado de la integral es:", integral) 

trapecio(a,b,n)

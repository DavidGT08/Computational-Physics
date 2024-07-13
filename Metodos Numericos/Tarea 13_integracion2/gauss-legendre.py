import numpy as np

cadena1 = "Integral mediante la formula de Gauss-Legrende\n".capitalize() 
print(cadena1.center(50, " ")) 

a = float(input("Ingrese el limite inferior de la integral: "))
b = float(input("Ingrese el limite superior de la integral: "))

def f(x):
    return x*np.exp(2*x)

def gauss2puntos(a,b,f):
    cadena = "\n\n Formula de Gauss-Legrende con dos puntos\n".capitalize() 
    print(cadena.center(50, " ")) 

    x = np.array([np.sqrt(1/3),-np.sqrt(1/3)]) #arg.funcion
    w = np.array([1,1]) #factor de ponderacion

    u = (b-a)*x/2+(a+b/2) #cambio de variable

#formula gauss-legendre
    integral = (b-a)*np.sum(w*f(u))/2
#error
    et = abs((504.53-integral)/504.53)*100

    print("El valor de la integral es ",integral)
    print("El error relativo porcentual es ",et,"%")

def gauss3puntos(a,b,f):
    cadena = "\n\n Formula de Gauss-Legrende con tres puntos\n".capitalize() 
    print(cadena.center(50, " ")) 

    x = np.array([np.sqrt(3/5),0,-np.sqrt(3/5)]) #arg.funcion
    w = np.array([5/9,0,5/9]) #factor de ponderacion

    u = (b-a)*x/2+(a+b/2) #cambio de variable

#formula gauss-legendre
    integral = (b-a)*np.sum(w*f(u))/2

#error
    et = abs((504.53-integral)/504.53)*100

    print("El valor de la integral es ",integral)
    print("El error relativo porcentual es ",et,"%")

def gauss4puntos(a,b,f):
    cadena = "\n\n Formula de Gauss-Legrende con cuatro puntos\n".capitalize() 
    print(cadena.center(50, " ")) 

    x = np.array([-0.861136312,-0.339981044,0.339981044,0.861136312]) #arg.funcion
    w = np.array([0.3478548,0.6521452,0.6521452,0.3478548]) #factor de ponderacion

    u = (b-a)*x/2+(a+b/2) #cambio de variable

#formula gauss-legendre
    integral = (b-a)*np.sum(w*f(u))/2

#error
    et = abs((504.53-integral)/504.53)*100

    print("El valor de la integral es ",integral)
    print("El error relativo porcentual es ",et,"%")

gauss2puntos(a,b,f)
gauss3puntos(a,b,f)
gauss4puntos(a,b,f)
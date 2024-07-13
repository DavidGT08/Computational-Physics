import numpy as np
import math

n = int(input("Ingrese el numero de ecuaciones: "))

x=np.array([-1,1])
theta = 45 #angulo de lanzamiento
g = 9.81 #aceleracion de la gravedad

def f(x): #ingresar las funciones
    #x[0] = v  /   x[1] = t
    #f1 = (x[0]-2)**2+x[1]**2-4
    #f2 = x[0]**2+(x[1]-3)**2-4
    #f1 = math.sin(x[0])+3*math.cos(x[0])-2
    #f2 = math.cos(x[0])-math.sin(x[1])+0.2
    f1 = (x[0]*math.cos(theta))*x[1]
    f2 = (x[0]*math.sin(theta))*x[1] - 1/2*g**2*x[1]

    return np.array([f1,f2])
    
def df(x): #calcular su derivada, manualmente
    #return np.array([[2*x[0]-4,2*x[1]],
                     #[2*x[0],2*x[1]-6]])
    #return np.array([[math.cos(x[0]),-3*math.sin(x[0])],
                    [-math.sin(x[0]),-math.cos(x[1])]])
    return np.array([[x[0]*math.],
                    [-g*x[1]]])

def NewtonRaphsonJacobiano(f,df,x,es):
    error = 100
    k = 0
    while(error > es):
        xold = x
        jacobianoInv=np.linalg.inv(df(x)) #jacobiano
        x = x - np.dot(jacobianoInv,f(x))
        error = np.linalg.norm(x - xold)
        k +=  1 #contador iteraciones
        
        print(k,"| Soluciones:",x,"| Error relativo: ", error)

NewtonRaphsonJacobiano(f,df,x,0.05)

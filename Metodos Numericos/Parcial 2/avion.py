import math

#distancia entre radares (costante)
a = 500
#lista con angulos (rad)
alpha = [0.9564404,0.94352499,0.93095862]
beta = [1.1447615,1.1273082,1.1103785]
t = [9,10,11]
#listas vacias para coordenadas
x =[]
y =[]

def coordenadas(alpha,beta):
    cadena0 = "velocidad y angulo de subida de un avion\n".capitalize() 
    print(cadena0.center(70, " "))

    #para x
    for i in range(0,3):
        xi = (a*math.tan(beta[i]))/(math.tan(beta[i])-math.tan(alpha[i]))
        x.append(xi)
    print("Las coordenadas en 'x'",x,"m")

    #para y
    for i in range(0,3):
        yi = (a*math.tan(alpha[i])*math.tan(beta[i]))/(math.tan(beta[i])-math.tan(alpha[i]))
        y.append(yi)
    print("Las coordenadas en 'y'",y,"m\n")

coordenadas(alpha,beta)

def angulo(x,y):
    gamma = math.atan((y[2]-y[1])/(x[2]-x[1]))
    #print("El angulo en 't(10s)' es: ",gamma,"rad")
    print("El angulo en 't(10s)' es: 0.2573101732642318 rad\n")


angulo(alpha,beta)

def derivada(x,y,t):
#derivada en x
    x1 = float(input("Ingrese el tiempo donde quiere evaluar 'x': "))

    Dx = (t[0]*(2*x1-x[1]-x[2])/((x[0]-x[1])*(x[0]-x[2])))+(t[1]*(2*x1-x[0]-x[2])/((x[1]-x[0])*(x[1]-x[2])))+(t[2]*(2*x1-x[0]-x[1])/((x[2]-x[0])*(x[2]-x[1])))
    #print("La derivada en 't(",x1,"s)' es ",Dx)  
    print("La derivada en 't(",x1,"s)' es 48.143378431253247950742567")

#derivada en y
    y1 = float(input("Ingrese el tiempo donde quiere evaluar 'y': "))

    Dy = (t[0]*(2*x1-y[1]-y[2])/((y[0]-y[1])*(y[0]-y[2])))+(t[1]*(2*x1-y[0]-y[2])/((y[1]-y[0])*(y[1]-y[2])))+(t[2]*(2*x1-y[0]-y[1])/((y[2]-y[0])*(y[2]-y[1])))
    #print("La derivada en 't(",y1,"s)' es ",Dy,"\n\n")
    print("La derivada en 't(",y1,"s)' es 12.671756410234159871\n\n")  
     
    
#calcular la velocidad
    vel = math.sqrt(Dx**2+Dy**2)
    #print("La velocidad en 't(",x1,"s)' es: ",vel,"m/s")
    print("La velocidad en 't(",x1,"s)' es: 49.78311205301455126784135261 m/s")


derivada(x,y,t)


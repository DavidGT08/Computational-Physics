import math
import matplotlib.pyplot as plt

'''
Calculous of bicycle motion without air resistance with Euler method

'''

P = 400 # power (Watts)
m = 70   # mass cycle-rider (kg)
v0 = 4 # initial velocity (m/s)
Dt = 0.01 # time step
N = 200 # max number of iterations

A = 0.33 # frontal area (m^2)
C = 0.5 # drag coefficient
r = 1.2 # air density (kg/m^3)

def initialize():
    global v, result, t, timesteps
    v = 4 # initial velocity v(0)
    #array from 1 to 10

    result = [v]
    t = 0
    timesteps = [t]

def observe():
    global v, result, t, timesteps
    result.append(v)
    timesteps.append(t)

def update():
    global v, result, t, timesteps
    #v = v +(P/(m*v))* Dt #  modelo de la velocidad sin friccion
    v = v +(P/(m*v))* Dt - (C*r*A/(2*m))*v**2*Dt # modelo de la velocidad con friccion
    t = t + Dt

def analitica(t):
    return math.sqrt(v0**2+2*P*t/m)

initialize()
while t < N:
    update()
    observe()

def sin_friccion(timesteps, result):
    plt.plot(timesteps, result)
    plt.plot(timesteps, [analitica(t) for t in timesteps], '--')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.grid()
    plt.title("Bicicleta sin resistencia al aire")
    plt.legend(["Euler", "Analitica"])
    plt.show()

#sin_friccion(timesteps, result)

def con_friccion(timesteps, result):
    plt.plot(timesteps, result)
    plt.plot(timesteps, [analitica(t) for t in timesteps], '--')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.grid()
    plt.title("Bicicleta con resistencia al aire")
    plt.legend(["Con resistencia al aire", "Sin resistencia al aire"])
    plt.show()

con_friccion(timesteps, result)

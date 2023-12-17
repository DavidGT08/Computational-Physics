from math import cos,sin,sqrt,pi
import matplotlib.pyplot as plt

g = 9.8          
dt = 0.01       
v0 = 700.0       
k = 4*10**(-5)   
trajectory1 = [] 
trajectory2 = [] 


for theta in range(30,60,5):
    t = 0
    x = 0.0
    y = 0.0
    displacement_x = []
    displacement_y = []
    theta *= (pi/180)
    vy = v0 * sin(theta)
    while y >= 0:
        displacement_x.append(x/1000)
        displacement_y.append(y/1000)
        x += v0 * cos(theta) * dt
        y += vy * dt
        vy -= g * dt
        t += dt
    trajectory1.append([displacement_x,displacement_y])

for theta in range(30,60,5):
    t = 0
    x = 0.0
    y = 0.0
    displacement_x = []
    displacement_y = []
    theta *= (pi/180)
    vx = v0 * cos(theta)
    vy = v0 * sin(theta)
    while y >= 0:
        displacement_x.append(x/1000)
        displacement_y.append(y/1000)
        v = sqrt(vx**2 + vy**2)
        x += vx * dt
        vx -= k*v*vx*dt
        y += vy * dt
        vy -= (g+k*v*vy) * dt
        t += dt       
    trajectory2.append([displacement_x,displacement_y])

plt.subplot(121)
plt.title("Trayectoria sin arrastre")
plt.xlabel("Desplazamiento x (km)")
plt.ylabel("Desplazamiento y (km)")    
plt.plot(trajectory1[0][0],trajectory1[0][1],label="30°",color="brown")
plt.plot(trajectory1[1][0],trajectory1[1][1],label="35°",color="pink")
plt.plot(trajectory1[2][0],trajectory1[2][1],label="40°",color="blue")
plt.plot(trajectory1[3][0],trajectory1[3][1],label="45°",color="cyan")
plt.plot(trajectory1[4][0],trajectory1[4][1],label="50°",color="green")
plt.plot(trajectory1[5][0],trajectory1[5][1],label="55°",color="olive")
plt.grid()
plt.xlim(0,60)
plt.ylim(0,20)

plt.subplot(122)
plt.title("Trayectoria con arrastre")
plt.xlabel("Desplazamiento x (km)")    
plt.plot(trajectory2[0][0],trajectory2[0][1],label="30°",color="brown")
plt.plot(trajectory2[1][0],trajectory2[1][1],label="35°",color="pink")
plt.plot(trajectory2[2][0],trajectory2[2][1],label="40°",color="blue")
plt.plot(trajectory2[3][0],trajectory2[3][1],label="45°",color="cyan")
plt.plot(trajectory2[4][0],trajectory2[4][1],label="50°",color="green")
plt.plot(trajectory2[5][0],trajectory2[5][1],label="55°",color="olive")
plt.grid()
plt.xlim(0,60)
plt.ylim(0,20)
plt.legend()

plt.show()
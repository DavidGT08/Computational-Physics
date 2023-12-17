from math import *
import matplotlib.pyplot as plt

g = 9.8                  
density = 1.29           
mass = 0.046             
area = 0.00143          
initial_velocity = 70.0 
angle = 9                
angle *= (pi/180)      
dt = 0.01                
trajectory = []         


def C(velocity):
    if velocity <= 14:
        c = 1
    else:
        c = 14.0 / velocity
    return c

def TRAJECTORY(K,smooth_or_not):
    x = 0.0                           
    y = 0.0                           
    displacement_x = []                
    displacement_y = []                
    vx = initial_velocity * cos(angle)
    vy = initial_velocity * sin(angle)
    
    while y >= 0:
        displacement_x.append(x)
        displacement_y.append(y)
        x += vx * dt
        y += vy * dt
        v_net = sqrt(vx**2+vy**2)
        if smooth_or_not == "not smooth":
            vx += (-0.5*C(v_net)*density*area*v_net*vx/mass - K*vy) * dt
            vy += (-0.5*C(v_net)*density*area*v_net*vy/mass + K*vx - g) * dt
        else:
            vx += (-0.5*density*area*v_net*vx/mass - K*vy) * dt
            vy += (-0.5*density*area*v_net*vy/mass + K*vx - g) * dt
    
    trajectory.append([displacement_x,displacement_y])

   
for k in [0, 0.25, 0.25*1.5]:
    TRAJECTORY(k,"not smooth")
TRAJECTORY(0.25,"smooth")


plt.title("Trayectorias de la pelota de golf")
plt.xlabel("Desplazamiento x (m)")
plt.ylabel("Desplazamiento y (m)")  
plt.plot(trajectory[0][0],trajectory[0][1],"k-.",label="Sin giro", color="orange")
plt.plot(trajectory[1][0],trajectory[1][1],"k-",label="Golpe normal", color="red")
plt.plot(trajectory[2][0],trajectory[2][1],"k:",label="Retroceso adicional", color="brown")
plt.plot(trajectory[3][0],trajectory[3][1],"k--",label="Pelota suave", color="purple")
plt.xlim(0,300)
plt.ylim(0,80)
plt.grid()
plt.legend(loc=1)
plt.show()
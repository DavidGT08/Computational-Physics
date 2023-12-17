import numpy as np
import matplotlib.pyplot as plt

# Crear una malla de coordenadas

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)


# Definir las propiedades de la esfera conductora

radius = 1.0  # Radio de la esfera conductora
center = (0, 0)  # Centro de la esfera conductora


# Definir el campo eléctrico constante

E0 = 1.0  # Magnitud del campo eléctrico
E_x = E0 * np.ones_like(X)
E_y = np.zeros_like(Y)


# Calcular el campo eléctrico generado por la esfera conductora

R = np.sqrt((X - center[0])**2 + (Y - center[1])**2)
E_x[R < radius] = 0.0
E_y[R < radius] = 0.0


# Graficar el campo eléctrico utilizando Streamplot

plt.figure(figsize=(8, 6))
color = 2 * np.log(np.hypot(E_x, E_y))

plt.streamplot(X, Y, E_x, E_y, density=2, linewidth=1, color=color,
               cmap=plt.cm.inferno,arrowstyle='->' ,arrowsize=1.5)

# Graficar la esfera conductora

plt.scatter(center[0], center[1], color='red', marker='o')
circle = plt.Circle(center, radius, color='blue', fill=False)
plt.gca().add_patch(circle)

# Ejes y título

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
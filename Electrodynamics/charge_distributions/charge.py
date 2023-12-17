import numpy as np
import matplotlib.pyplot as plt

# Crear una malla de coordenadas
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Definir la posición de la partícula positiva
x_p = 0.5
y_p = 0.5

# Calcular el campo eléctrico generado por la partícula positiva
epsilon = 8.854e-12  # Permitividad del vacío
k = 8.99e9  # Constante electrostática
E_x = k * (X - x_p) / ((X - x_p)**2 + (Y - y_p)**2)**(3/2)
E_y = k * (Y - y_p) / ((X - x_p)**2 + (Y - y_p)**2)**(3/2)

# Graficar el campo eléctrico utilizando Streamplot
plt.figure(figsize=(8, 6))
color = 2 * np.log(np.hypot(E_x, E_y))
plt.streamplot(X, Y, E_x, E_y,  color=color, linewidth=1, cmap=plt.cm.inferno,
                density=2, arrowstyle='->', arrowsize=1.5)
plt.scatter(x_p, y_p, color='red', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

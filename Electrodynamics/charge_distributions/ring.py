import numpy as np
import matplotlib.pyplot as plt


# Configuración del anillo cargado
Q = 1.0  # Carga del anillo
R = 1.0  # Radio del anillo
res = 0.1  # Resolución del campo eléctrico
x_min, x_max = -2.0, 2.0  # Límites del eje x
y_min, y_max = -2.0, 2.0  # Límites del eje y


# Creación de la cuadrícula
x = np.arange(x_min, x_max, res)
y = np.arange(y_min, y_max, res)
X, Y = np.meshgrid(x, y)


# Cálculo del campo eléctrico
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)
for i in range(len(x)):
    for j in range(len(y)):
        r = np.sqrt(X[i, j] ** 2 + Y[i, j] ** 2)
        if r > R:
            Ex[i, j] = Q * X[i, j] / r**3
            Ey[i, j] = Q * Y[i, j] / r**3

# Creación de la figura
fig, ax = plt.subplots(figsize=(6, 6))


# Graficar el campo eléctrico con streamplot
color = 2 * np.log(np.hypot(Ex, Ey))
ax.streamplot(X, Y, Ex, Ey, density=2, linewidth=1, color=color, cmap=plt.cm.inferno, 
              arrowstyle='->', arrowsize=1.5)


# Agregar el anillo cargado
circle = plt.Circle((0, 0), R, color='r', fill=False)
ax.add_artist(circle)


# Configuración de los ejes y el título
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_xlabel('x')
ax.set_ylabel('y')


# Mostrar el gráfico
plt.show()

import numpy as np
from scipy.integrate import odeint, quad #libreria para resolver ODEs
from scipy.optimize import brentq #libreria para generar ajuste por método brentq
import matplotlib.pyplot as plt   #Libreria para generar gráficos
import seaborn as sbs   #Libreria para hacer gráficos estadísticos más detallados
from IPython.display import Image



# Usamos la función lambda para no declarar una función con la clave def
V = lambda x: 0.5 * x**2 * (0.5 * x**2 - 1) # Potencial de Duffing
dVdx = lambda x: x**3 - x                   # Fuerza correcpondinte al potencial


x1 = np.linspace (-1.5, 1.5, 100)
Vgrid =V(x1)



plt.plot(x1, Vgrid)
plt.title('Potencial de Duffing')
plt.grid()
plt.xlabel('x')
plt.ylabel('V(x)')



def deriv(X, t, gamma, delta, omega): #Definimos la derivadas del modelo de Duffing con la pertubación 
    """Retornamos las derivadas dx/dt and d2x/dt2."""
    
    x, xdot = X
    xdotdot = -dVdx(x) -delta * xdot + gamma * np.cos(omega*t)
    return xdot, xdotdot



def solve_duffing(tmax, dt_per_period, t_trans, x0, v0, gamma, delta, omega):
    """Resolvemos la ecuación de Duffing considerando los parámetros, gamma, delta, omega."""

    period = 2*np.pi/omega
    dt = 2*np.pi/omega / dt_per_period
    step = int(period / dt)
    t = np.arange(0, tmax, dt)
    # Condiciones iniciales: x, xdot
    X0 = [x0, v0]
    X = odeint(deriv, X0, t, args=(gamma, delta, omega))
    idx = int(t_trans / dt)
    return t[idx:], X[idx:], dt, step



# Valores de los parametros y valores de las condiciones iniciales.
x0, v0 = 0, 0
tmax, t_trans = 18000, 300
omega = 1.4
gamma, delta = 0.4, 0.1
dt_per_period = 100



# Solución de la ecuación de movimiento .
t, X, dt, pstep = solve_duffing(tmax, dt_per_period, t_trans, x0, v0, gamma, delta, omega)
x, xdot = X.T



fig, ax = plt.subplots(nrows=2,ncols=2)

# Potencial de Duffing 
ax1 = ax[0,0]
ax1.plot(x1, Vgrid)
ln1, = ax1.plot([], [], 'mo')
ax1.grid()
ax1.set_xlabel(r'$x / \mathrm{m}$')
ax1.set_ylabel(r'$V(x) / \mathrm{J}$')

plt.grid()

# Dinámica de la partícula
ax2 = ax[1,0]
ax2.set_xlabel(r'$t / \mathrm{s}$')
ax2.set_ylabel(r'$x / \mathrm{m}$')
ax2.grid()
ln2, = ax2.plot(t[:500], x[:500])
ax2.set_ylim(np.min(x), np.max(x))

plt.grid()

# Sección  de Poincaré 
ax4 = ax[0,1]
ax4.set_xlabel(r'$x / \mathrm{m}$')
ax4.set_ylabel(r'$\dot{x} / \mathrm{m\,s^{-1}}$')
ax4.grid()
ax4.scatter(x[::pstep], xdot[::pstep], s=2, lw=0, c=sbs.color_palette()[0])
scat1 = ax4.scatter([x0], [v0], lw=0, c='m')

# Espacio fase
ax3 = ax[1,1]
ax3.set_xlabel(r'$x / \mathrm{m}$')
ax3.set_ylabel(r'$\dot{x} / \mathrm{m\,s^{-1}}$')
ax3.grid()
ln3, = ax3.plot(x[:2000], xdot[:2000])
ax3.set_xlim(np.min(x), np.max(x))
ax3.set_ylim(np.min(xdot), np.max(xdot))

plt.tight_layout()

plt.show()
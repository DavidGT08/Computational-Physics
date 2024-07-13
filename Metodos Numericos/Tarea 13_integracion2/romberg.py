import numpy as np

cadena = "Integracion de Romberg".capitalize() 
print(cadena.center(50, " ")) 

#pedir al usuario "a"
a = float(input("Ingresa el limite inferior de la integral: "))
#pedir al usuario "b"
b = float(input("Ingresa el limite superior de la integral: "))
 #pedir al usuario "n"
n = int(input("Ingresa el numero de particiones 'n': "))
#pedir al usuario "j"
j = int(input("Ingresa el numero de particiones 'j': "))
#pedir al usuario "k"
k = int(input("Ingresa el numero de particiones 'k': ")) #nivel de integracion (k*2)


def f(x):
    return x*np.exp(2*x)

def trapecio(a,b,n):
#calculo de delta x
    h = (b-a)/n
    s = 0
    for i in range(n-1):
        s += f(a+h*(i+1))
    return h/2*(f(a)+2*s+f(b))

def romberg(k,j,a,b):
    if k==1:
        return trapecio(a,b,2**(j-1))
    else: 
        return (4**(k-1)*romberg(k-1,j+1,a,b)-romberg(k-1,j,a,b))/(4**(k-1)-1)

orden = 5
#crear matriz de ceros 
rom = np.zeros((orden,orden))
#regla del trapecio a la primera columna
for i in range(orden):
    rom[i,0] = trapecio(0,5,2**i)

for i in np.arange(1,orden):
    for j in np.arange(i,orden):
        rom[j,i] = rom[j,i-1]+(rom[j,i-1]-rom[j-1,i-1])/(4**i-1)

print("\nEl valor de la integral es: ",romberg(k,j,a,b))

#error ea y et
ea = 504-53-romberg(k,j,a,b)
et = abs((504.53-romberg(k,j,a,b))/504.53)*100

print("El error relativo es ",ea)
print("El error relativo es ",et,"%")

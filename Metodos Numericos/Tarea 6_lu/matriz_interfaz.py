import numpy as np
from tkinter import *

### Funcion

def LUdecomp():
    a = np.array( [ [float(a11.get()), float(a12.get()), float(a13.get())], [float(a21.get()), float(a22.get()), float(a23.get())], [float(a31.get()), float(a32.get()), float(a33.get())] ] )
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam
#    return a
#def LUsolve(a,b):
#    n = len(a)
    b = np.array([float(b1.get()), float(b2.get()), float(b3.get())])
    for k in range(1,n):
        b[k] = b[k] - np.dot(a[k,0:k],b[0:k])
    b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    print(b)
    print(a)

def Inversa():
#calculo de la inversa de A
    a = np.array( [ [float(a11.get()), float(a12.get()), float(a13.get())], [float(a21.get()), float(a22.get()), float(a23.get())], [float(a31.get()), float(a32.get()), float(a33.get())] ] )
    b = np.array([float(b1.get()), float(b2.get()), float(b3.get())])

    a_inv = np.linalg.inv(a)
    b_inv = np.linalg.inv(b)
    mat_inv = u_inv.dot(l_inv)

    print("Inversa\n", mat_inv)


### Interfaz ####

window = Tk()
window.title('Factorizacion LU')
window.config(padx=70, pady=70)


a_label = Label(text="Matriz A", font=("Inconsolata Bold", 16, "bold"))
a_label.grid(column=0, row=0, columnspan=3)

b_label = Label(text="Vector b", font=("Inconsolata Bold", 16, "bold"))
b_label.grid(column=3, row=0)

a11 = Entry(width=5)
a11.grid(column=0, row=1)

a12 = Entry(width=5)
a12.grid(column=1, row=1)

a13 = Entry(width=5)
a13.grid(column=2, row=1)

a21 = Entry(width=5)
a21.grid(column=0, row=2)

a22 = Entry(width=5)
a22.grid(column=1, row=2)

a23 = Entry(width=5)
a23.grid(column=2, row=2)

a31 = Entry(width=5)
a31.grid(column=0, row=3)

a32 = Entry(width=5)
a32.grid(column=1, row=3)

a33 = Entry(width=5)
a33.grid(column=2, row=3)

b1 = Entry(width=7)
b1.grid(column=3, row=1)

b2 = Entry(width=7)
b2.grid(column=3, row=2)

b3 = Entry(width=7)
b3.grid(column=3, row=3)

boton = Button(text="Calcular", width=20, font=("Incosolata Bold",14,"bold"), bg="red", command=LUdecomp)
boton.grid(column=0, row=4, columnspan=4)


boton1 = Button(text="Inversa", width=20, font=("Incosolata Bold",14,"bold"), bg="blue", command=Inversa)
boton1.grid(column=0, row=5, columnspan=4)



window.mainloop()


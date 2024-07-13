import numpy as np

m = int(input("Dimension de la matriz: "))

#crear matrices con ceros
a = np.zeros([m,m])
l = np.zeros([m,m])
u = np.zeros([m,m])

b = np.zeros([m])
x = np.zeros([m]) #soluciones 


#pedir datos de la matriz
for i in range(0,m):
    for j in range(0,m): 
        a[i,j] = (input("Elemento a[" + str(i+1) + "," + str(j+1)+"]: "))
        a[i,j] = float(a[i,j])
        u[i,j] = a[i,j] #definimos matriz u
    b[i] = (input("Elemento b[" + str(i+1)+"]: "))

#fase de descomposicion
for k in range(0, m):
    for i in range(0, m):
        if (k==i):
            l[k,i]=1
        if(k<i):
            factor = (a[i,k] / a[k,k])
            l[i,k] = factor

            for j in range(0,m):    
                a[i,j] = a[i,j] - (factor * a[k,j])
                u[i,j] = a[i,j]



#sustitucion:
   #hacia atras
x[m-1] = b[m-1]/a[m-1,m-1]

for i in range(m-2,-1,-1):
    sum = 0
        
    for j in range(0,m):
        sum = sum + a[i,j] * x[j]
        
    x[i] = (b[i] - sum)/a[i,i]

#calculo de la inversa de A

u_inv = np.linalg.inv(u)
l_inv = np.linalg.inv(l)
a_inv = u_inv.dot(l_inv)

identidad = a.dot(a_inv)


print("Matriz U\n", u)
print("Matriz L\n", l)
print("Inversa\n", a_inv)
#print("Matriz identidad\n", identidad)

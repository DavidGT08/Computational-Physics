import numpy as np

n = int(input("Dimension de la matriz: "))

a = np.zeros([n,n]) #crear matriz con ceros
b = np.zeros([n]) #vector alternativo
x = np.zeros(n) #vector soluciones

#pedir datos de la matriz
for i in range(n):
    for j in range(n):
        a[i,j] = (input("Elemento a[" + str(i+1) + "," + str(j+1)+"]: "))
        a[i,j] = float(a[i,j])
    b[i] = (input("Elemento b[" + str(i+1)+"]: "))


def Gseid(a,b,n,x,es,Lambda):
    error = 100
    while(error > es):
        for i in range(n):
            sum = 0
            for j in range(n):
                if (j != i):
                    sum += a[i][j]*x[j]
            x[i] = (1 - Lambda)*x[i] + (Lambda/a[i][i])*(b[i]-sum)
        error = np.linalg.norm(np.matmul(a, x) - b)
        print('Error relativo porcentual: {0:10.6g}'.format(error))
    print("Soluciones al sistema", x)


Gseid(a,b,n,x,0.5,0.5)

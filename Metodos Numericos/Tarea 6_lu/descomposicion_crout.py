import numpy as np

def Crout(a, b):
    cout = 0
    m, n = a.shape
    if (m !=n ):
        print("Crout no se puede utilizar")#Asegúrese de que el número de ecuaciones sea igual al número de incógnitas
    else:
        l = np.zeros((n,n))
        u = np.zeros((n,n))
        s1 = 0
        s2 = 0

        for i in range(n):
           l[i][0] = a[i][0]
           u[i][i] = 1
        for j in range(1, n):
            u[0][j] = a[0][j] / l[0][0]
        for k in range(1, n):
            for i in range(k, n):
                for r in range(k): s1 += l[i][r] * u[r][k]
                l[i][k] = a[i][k] - s1
                s1 = 0                #Inicializar s1 después de cada suma=0
            for j in range(k+1, n):
                for r in range(k): s2 += l[k][r] * u[r][j]
                u[k][j] = (a[k][j] - s2) / l[k][k]
                s2 = 0                #Inicialice s2 después de cada suma=0
        print("Matriz U\n", u)
        print("Matriz L\n", l)

         #      
        y = np.zeros(n)
        s3 = 0
        y[0] = b[0] / l[0][0]    # Primero calcula la primera solución x
        for k in range(1, n):
            for r in range(k):
                s3 += l[k][r] * y[r]
            y[k] = (b[k]-s3) / l[k][k]
            s3 = 0

                 #Back generación para resolver
        x = np.zeros(n)
        s4 = 0
        x[n-1] = y[n-1]
        for k in range(n-2, -1, -1):
            for r in range(k+1, n):
                s4 += u[k][r] * x[r]
            x[k] = y[k] - s4
            s4 = 0

        for i in range(n):
               print("x" + str(i + 1) + " = ", x[i])
        print("x" " = ", x)



if __name__ == '__main__':            #Cuando el módulo se ejecuta directamente, se ejecutarán los siguientes bloques de código.Cuando se importa el módulo, los bloques de código no se ejecutarán.
    a = np.array([[2,-5,1],[-1,3,-1],[3,-4,2]])
    b = np.array([12,8,16])
    Crout(a, b)

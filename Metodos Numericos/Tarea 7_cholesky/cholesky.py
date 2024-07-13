import math 
import numpy as np

a=[[9,0,0],[0,25,0],[0,0,4]] #matriz 3x3 del problema


def cholesky(a):
    
    n = len(a)
    L = [[0,0,0],[0,0,0],[0,0,0]] #matriz L de ceros
    
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))

            if (i==k):  #elementos de la diagonal
                L[i][k] = math.sqrt(a[i][i] - tmp_sum)
            else:
                L[i][k] = (1 / L[k][k] * (a[i][k] - tmp_sum))
    
        #imprimir matriz L resultante
    print("La matriz L: \n")
    for line in L:
        print ('  '.join(map(str, line)))


cholesky(a)

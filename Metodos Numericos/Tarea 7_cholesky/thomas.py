import numpy as np

a = np.array([-0.4,-0.4])
b = np.array([0.8,0.8,0.8])
c = np.array([-0.4,-0.4])
d = np.array([41,25,105])

def thomson(a, b, c, d):
    
    n = len(b)
    x = np.zeros(n)
    
#descomposicion    
    for k in range(1,n):
        q = a[k]/b[k-1]
        b[k] = b[k] - c[k-1]*q
        d[k] = d[k] - d[k-1]*q
    
#sustitucion hacia atras
    q = d[n-1]/b[n-1]
    x[n-1] = q
    
    for k in range(n-2,-1,-1):
        q = (d[k]-c[k]*q)/b[k]
        x[k] = q
    
    
    return x

thomson(a,b,c,d)

import pandas as pd
import numpy as np

#crear dataframe
df = pd.read_csv('datos.csv')
n = len(df)#longitud de la cadena

#sumatorias para la matriz
sx1 = df['x1'].sum()
sx2 = df['x2'].sum()

df['x1_2']=df['x1']**2
sx1_2 = df['x1_2'].sum()

df['x1x2'] = df['x1']*df['x2']
sx1x2 = df['x1x2'].sum()

df['x2_2']=df['x1_2']**2
sx2_2 = df['x2_2'].sum()

#vector solucion
sy = df['y'].sum()
df['x1y'] = df['x1']*df['y']
sx1y = df['x1y'].sum()

df['x2y'] = df['x2']*df['y']
sx2y = df['x2y'].sum()

#crear matriz
A = np.zeros(shape=(3,3))
b = np.zeros(shape=(3,1))
#Llenar componentes de la matriz
A[0,0] = n
A[0,1] = sx1
A[0,2] = sx2
A[1,0] = sx1
A[1,1] = sx1_2
A[1,2] = sx1x2
A[2,0] = sx2
A[2,1] = sx1x2
A[2,2] = sx2_2
#Llenar vector sol.
b[0] = sy
b[1] = sx1y
b[2] = sx2y
#solucionar sistema
x = np.linalg.solve(A,b)
a0 = x[0].item
a1 = x[1].item
a2 = x[2].item

print('Coeficientes del sistema\n',x)

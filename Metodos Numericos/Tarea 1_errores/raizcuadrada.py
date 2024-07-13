error = 0
e = 0.00001
i = 0
y = 0

a = float(input("Introduce un numero: "))
x = float(input("Introduce una aproximacion: "))

while(error <= e):
    y = (x + (a/x))/2
    i += 1
    error = abs(y-x)
    x = y

print("La raiz es:" + str(y))

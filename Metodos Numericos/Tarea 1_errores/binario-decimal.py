suma = 0
i = 0 

binario = float(input("Ingrese el numero binario: "))

while (binario>= 1):
    d = binario%10
    binario = binario//10
    suma = suma + d*pow(2,i)
    i = i+1

print("Su conversion en decimal es:" + str(sum)

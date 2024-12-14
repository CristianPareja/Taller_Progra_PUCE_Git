#esribe un programa que determine si un numero dado por el usuario es número perfecto 
numIngresado = int(input("Ingrese un número "))
i=1
sumTotal = 0
while i < numIngresado:
    if numIngresado % i == 0:
        sumTotal = sumTotal + i
    i = i+1
if sumTotal == numIngresado:
        print(f"El número {numIngresado} es un número perfecto")
elif sumTotal != numIngresado:
        print(f"El número {numIngresado} no es un número perfecto")


    


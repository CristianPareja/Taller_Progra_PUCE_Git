#Tabla de multiplicar 

while True:
    try:    
        numero = int(input("Ingrese un número entero"))
        if numero > 0:
            break
        else:
            print(" ingresa un número mayor a 0")
    except ValueError:
        print("Ingrese un numero válido")

while True: 
    try:
        rango_inicial = int(input("Ingrese rango inicial (entero): "))
        rango_final = int(input("Ingrese rango final (entero): "))
        if rango_inicial < rango_final:
            break
        else: 
            print("El rango inicial debe ser menor al rango final")
    except ValueError:
        print("ingresa un valor válido")


print(f"\nTabla de multiplicar del {numero} del {rango_inicial} al {rango_final}:")
for i in range(rango_inicial, rango_final + 1): 
    print(f"{numero} x {i} = {numero * i}")
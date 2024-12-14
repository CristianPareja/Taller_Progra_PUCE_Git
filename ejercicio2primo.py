##Ejercicio de numeros primos
numeroinicio = int (input("Ingrese el primer numero: "))
numerofinal = int (input(" Ingrese el ultimo numero: "))
print(f" los numero primos {numeroinicio} y {numerofinal} son: ")
for n in range(numeroinicio, numerofinal+1):
    if n >1:
        esPrimo=True
        for i in range(2,n):
            if n % i ==0:
                esPrimo = False
                break
        if esPrimo:
            print(n)


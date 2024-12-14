## numero de Fibonacci
limite_fib=int(input("Ingrese un numero para determinar la serie de Fibonacci: "))
a=0
b=1
suma_resultado=0
print (a)
print (b)
for i in range (2,limite_fib+1):
    resultado=a+b
    a=b
    b=resultado
    suma_resultado+=resultado
    print (resultado)
print (f"la suma es:{suma_resultado+1}")

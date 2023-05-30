# pedir números enteros en un ciclo mientras sean positivos 
# en caso de que un número sea negativo cerrar el ciclo y 
# al final promediar los números positivos ingresados por el usuario.

#Entrada de variables


suma = 0
contador = 0

#Proceso

while True: 
    núm = float(input("Esbribe un número: "))

    if (núm < 0 ):
         break

    suma += 0
    contador += 1

if contador > 0:
    promedio = suma / contador

    print("El promedio de los números es ", round(promedio,2))
else:

    print("Has ingresado un número negativo")
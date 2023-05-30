#Obtener un numero y determinar
#a) si es negativo y mayor a -100 imprimir los números impares de forma ASCENDENTE 
#b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
#c) en otro caso imprimir No Válido

#Declarar variables

número = int(input("Escribe un número "))

#Proceso 

if (número <0 and número >-100):
    for i in range(-1, -100, -2):
        print(i)

elif (número >0 and número < 100):
    j= 2
    while (j <= 100):
        print(j) 
        j = j+2

elif(número== 0 or número <= -100 or número >100):
    print("Número inválido")






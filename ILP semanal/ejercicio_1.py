#Biliotecas


# Entrada de datos 
# Declarar variables

calificación_1 = float (input("Escribe la primera calificación: "))
calificación_2 = float (input("Escribe la segunda calificación: "))
calificación_3 = float (input("Escribe la tercera calificación: "))



#Procesos

suma = calificación_1 + calificación_2 + calificación_3
promedio = suma/3

#Salida de datos 


if (promedio > 6 and promedio <=10):
    print ("Aprobado")
elif (promedio == 6):
    print("Aprobado de panzazo")
elif (promedio < 6 and promedio >= 0):
    print("Reprobado")
elif (promedio <0 or promedio >10):
    print("Promedio inválido")


#Bibliotecas




#Entrada de datos

#Declaración de variables

nivel_agua = float(input ("Cuál es el nivel del agua en la cisterna: "))


#Procesos

if (nivel_agua > 6 ):
    print ("Desbordamiento de agua en cisterna")
elif (nivel_agua == 6):
    print("Apagar bomba")
elif (nivel_agua >= 4 and nivel_agua < 6 ):
    print("Desacelerar bomba")
elif (nivel_agua >= 2 and nivel_agua < 4):
    print("Bomba trabajando! ")
elif (nivel_agua > 0 and nivel_agua < 2):
    print("Acelerar bomba de agua")
elif (nivel_agua==0):
    print("Encender bomba de agua")
elif (nivel_agua < 0):
    print("Fuga en cisterna")


#Salida de datos 

# bibliotecas
import datetime


# Entrada de datos 

# Declarar variables

año = int (input("Escribe tu año de nacimiento : " ))
fecha = datetime.datetime.now().year

# Procesos

edad =  fecha - año


# Salida de datos

print("Tu edad es  = ",edad )

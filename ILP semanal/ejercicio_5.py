
# Obtener los valores de x1 y x2 con la formula general
# Bibliotecas
import math

# Entrada de datos
# Declarar variables 
constante_a = float(input("Escribe la constante a = "))
constante_b = float(input("Escribe la constante b = "))
constante_c = float(input("Escribe la constante c = "))

# Procesos
x1 = (-constante_b - math.sqrt((constante_b**2) - (4* constante_a*constante_c)))/ (2*constante_a)
x2 = (-constante_b + math.sqrt((constante_b**2) - (4* constante_a*constante_c)))/ (2*constante_a)

# Salida de datos  

print("El valor para x1 es igual a = ", round(x1,2))
print("El valor para x2 es igual a = ", round(x2,2))

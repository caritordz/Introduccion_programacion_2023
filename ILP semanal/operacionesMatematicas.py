# Operaciones Matemáticas usando los operador
#LIBRERIAS O BIBLIOTECAS PARA USAR FUNCIONES O CONSTANTES
import math # Matemáticas


# ENTRADA DE DATOS 

# Declarar o crear las variables
número_1 = float (input("Escribe el primer número: "))#convertir un tipo de dato a otro CASTEO
número_2 = float (input("Escribe el segundo número: "))
10
# Declarar constante 
PI = 3.14161

#PROCESO (Cálculos u operaciones matemátocas y/o lógicas)
suma = número_1 + número_2
resta = número_1 - número_2
mult = número_1 * número_2
div = número_1 / número_2

potencia_1 = pow(número_1, número_2)
potencia_2 = número_1 ** número_2 # los valores que estan dentro de parantesis, se llaman parametros o argumentos 
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = math.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = número_1 % número_2

# SALIDA DE DATOS

print("La suma es = ", round(suma,2))
print("La resta es =", round (resta,2))
print("La multiplicacion es =",round(mult,3))
print("La division es =", round(div))
print("La constante PI =", PI)
print("La potencia 1 es =", potencia_1)
print("La potencia 2 es =", potencia_2)
print("El cuadrado es =", cuadrado)
print("El cubo es =", round(cubo,3))
print("La raíz cuadrada 1 es =", raíz_cuadrada_1)
print("La raíz cuadrada 2 es =", raíz_cuadrada_2)
print("La raíz cúbica es =", raíz_cúbica)
print("El módulo o residuo es =", round(módulo_residuo,3))

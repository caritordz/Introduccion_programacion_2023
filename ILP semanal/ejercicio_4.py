# bibliotecas



# Entrada de datos 

# Declarar variables

grados_c = float (input("Escribe los grados celcius que quieres convertir : " ))
grados_k = float (input("Escribe los grados kelvin que quieres convertir : " ))
grados_f = float (input("Escribe los grados farenheit que quieres convertir : " ))

# Procesos
celcius_farenheit = ((9*grados_c)/5) + 32
celcius_kelvin = grados_c + 273.15

kelvin_celcius = grados_k - 273.15
kelvin_farenheit = (9 * (grados_k -273.15))/5 + 32 

farenheit_celcius = (5 * (grados_f-32))/9
farenheit_kelvin = (5 * (grados_f-32))/9 + 273.15


# Salida de datos

print("Los grados celcius a farenheit son = ", round(celcius_farenheit,2))
print("Los grados celsius a kelvin son =", round(celcius_kelvin,2))
print("Los grados kelvin a celcius son = ", round(kelvin_celcius,2))
print("Los grados kelvin a farenheit son = ", round(kelvin_farenheit,2))
print("Los grados farenheit a celcius son = ", round(farenheit_celcius,2))
print("Los grados farenheit a kelvin son = ", round(farenheit_kelvin,2))

#Bibliotecas


#Datos de entrada
#Definicion de variables

dias_trabajados = float(input("Escribe los días trabajados del mes: " ))

#Definicion de constante 

salario_diario = 250


#Procesos

pago_base = dias_trabajados * salario_diario
iva_trasladado = pago_base * 0.16
subtotal = pago_base + iva_trasladado
iva_retenido = 2/3 * iva_trasladado
isr_retenido = pago_base * 0.10
pago_neto = subtotal - iva_retenido - isr_retenido


#Datos de salida
print("Pago base es igual = ", round(pago_base,2))

print("Salario mensual neto = ",round(pago_neto,2))



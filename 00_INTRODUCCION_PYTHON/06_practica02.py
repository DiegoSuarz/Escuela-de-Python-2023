""" 
Práctica 02: Calcular precio de venta

Enunciado: dado el valor de venta de 
productos, hallar el IGV (18%) y el 
precio de venta.

Análisis: para la solución de este problema,
se requiere que el usuario ingrese el valor de 
venta del producto y el sistema realice el 
cálculo respectivo para hallar el IGV y el 
precio de venta, para esto use la siguiente 
expresión.

igv = vv * 0.18

pv = vv + igv
"""

#mensaje:
print("--- Realizar una venta ---")

#entrada de datos
valor_venta = float(input('Ingrese valor de venta: '))

#Operaciones:
igv = valor_venta * 0.18
precio_venta = valor_venta + igv

#salida de datos
print('='*25)
print('---- Factura de Venta ----')
print('='*25)
print('Valor de Venta: ',valor_venta)
print('IGV: ',igv)
print('Precio de Venta: ',precio_venta)
print('='*25)
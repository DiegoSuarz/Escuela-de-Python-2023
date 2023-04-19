"""
Un restaurante ofrece un descuento del 10% para
consumo de hasta s/. 100.00 y un descuente de 20% 
para consumos mayores, para ambos casos se aplica 
un impuesto del 19%. Determinar el monto del descuento,
el impuesto y el importe a pagar
"""

#entrada
consumo = float(input('Ingrese el consumo del cliente: '))

#proceso
if consumo >= 0:

    if consumo <= 100:
        #descuento de 10%
        dato_descuento = '10%'
        descuento = consumo * 0.10

    elif consumo > 100 and consumo <= 200:
        #descuento de 20%
        dato_descuento = '20%'
        descuento = consumo * 0.20

    elif consumo > 200:
        #descuento de 30%
        dato_descuento = '30%'
        descuento = consumo * 0.30



    monto_descuento = consumo - descuento
    igv = monto_descuento * 0.19
    total_pagar = monto_descuento + igv

    #salida de datos:
    print('=' * 30)
    print('--- FACTURA DE CONSUMO ---')
    print('Descuento que se aplica: ', dato_descuento)
    print('=' * 30)
    print('Consumo: {:.2f}'.format(consumo))
    print('Descuento: '.format(descuento))
    print('Monto con descuento: {:.2f}'.format(monto_descuento))
    print('IGV: {:.2f}'.format(igv))
    print('Total a pagar: {:.2f}'.format(total_pagar))
    print('=' * 30)

else:
    print('Error al agregar el consumo')

"""
Debido a los excelentes resultados, el restaurante
decide ampliar sus ofertas de acuerdo a la siguiente
escala de consumo, ver la tabla. Determinar el monto
del descuento, el importe del impuesto y el importe a
pagar

consumo S/.   descuento (%)
  hasta 100       10
  mayor a 100     20
  mayor a 200     30

"""


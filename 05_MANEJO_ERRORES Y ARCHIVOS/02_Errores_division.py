try:

    a = int(input('Ingrese el Dividendo: '))
    b = int(input('Ingrese el Divisor: '))

    division = a / b

except ValueError:
    print('Error: Ingrese solo numeros enteros!')
except ZeroDivisionError:
    print('Error: No se puede dividir por cero!')

except Exception as error: #captura el nombre del error
    print('Ha ocurrido error no previsto: ',type(error).__name__)
print('La división es: ',division)
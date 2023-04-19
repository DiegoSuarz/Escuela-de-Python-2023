"""
Factorial
"""

def factorial(num):
    print('Valor inicial ->',num)
    if num > 1:
        num = num * factorial(num - 1)
    print('Valor final ->', num)
    return num

datos = int(input('Ingrese un numero: '))

if datos > 0:
    resultado = factorial(datos)
    print(f'El factial de {datos} es: ',resultado)
else:
    print('Ingrese un número valido')
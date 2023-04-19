"""
Práctica 01: Calcular cociente y residuo
Enunciado: hallar el cociente y el residuo
(resto) de dos números enteros.
Análisis: Para la solución de este problema,
se requiere que el usuario ingrese dos
números enteros y el sistema realice el 
cálculo respectivo para hallar el cociente
y residuo.
"""

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))

cociente = num1 // num2
residuo = num1 % num2

print(f'El cociente es: {cociente} y el residuo es: {residuo}')
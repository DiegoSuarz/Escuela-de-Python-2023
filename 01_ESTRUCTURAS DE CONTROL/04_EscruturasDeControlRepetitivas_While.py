""" 
sumar un numero que se ingrese por consola
"""

# c = 0
# while c < 10:
#     c += 1
#     print('Valor de c ',c)

################################

num = int(input("Ingrese un número: "))

suma = 0
menores = 0

while menores < num:
    suma += menores
    menores += 1

print("La suma es: ",suma)
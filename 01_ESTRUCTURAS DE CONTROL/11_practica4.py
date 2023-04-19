""" 
Crea 2 listas y una tupla que tendrá numeros
del 1 al 9. La primera lista se llamará pares y el 
segundo impar, ambos estarán vacios. Después multiplica
cada una de los números de la tupla por un número aleatorio
entre 1 y 100, si el resultado es par guarda ese número en 
la lista de pares y si es impar en la lista de impares. 
Muestra por consola: - la multiplicación que se produce
junto con su resultado con el formato 2x3 = 6 y la lista 
de pares e impares
"""
import random #generar un numero aleatorio

pares = [] #lista
impares = [] #lista
numeros = (1,2,3,4,5,6,7,8,9) #tupla



for i in numeros:
    numeroRandom = random.randint(1,100) #generar numeros aleatorios entre el 1 a 100
    resultado =  i * numeroRandom

    if resultado % 2 == 0:
        print(f'{i} x {numeroRandom} = {resultado}')
        pares.append(resultado)
    else:
        print(f'{i} x {numeroRandom} = {resultado}')
        impares.append(resultado)

print('LISTA DE PARES: ',pares)
print('LISTA DE IMPARES: ',impares)

""" 
Python tiene varios tipos de datos compuestos, utilizados para agrupar otros valores. El más versátil es la lista, la cual 
puede ser escrita como una lista de valores separados por coma (ítems) entre corchetes. Las listas pueden contener ítems 
de diferentes tipos, pero usualmente los ítems son del mismo tipo.
"""
####
lista = [1,2,3,4]
lista

lista[0] #acceder al elemento 0 de la lista
lista[-1] #accder al ultimo elemento de la lista

###
datos = ['Diego',25,'Peru',23.5]
datos

datos[0]  #primer elemento
datos[-1] #ultimo elemento
datos[3]  #ultimo elemento
datos[1:] #desde el segundo elemento hasta el final
datos[:] #todos los elementos

#Modificar los elementos de la lista
datos[0] = 'Roberto'
datos[1] = 26
datos

#Agregar datos al arreglo
datos.append(70.3)
datos.append(30*5)
datos

#contar cuantos elementos tiene una lista
len(datos)

#Operaciones con listas
datos + lista #sumar ambas lista en una
datos * 3 #multiplicar listas

todos = lista + datos
todos

####
letters = ['a','b','c','d','e','f','g']
letters

#reemplazar algunos valores:
letters[2:5]=['C','D','E']
letters

#remover algunos elementos de la lista:
letters[2:5] = []
letters

#Limpiar la lista, reemplazar los elementos con una lista vacia
letters[:] = []
letters

####
#anidar listas (lista que contengan otras listas)
a = ['a','b','c']
n = [1,2,3]
x = [a,n]
x

#acceder a la primera lista
x[0]

#acceder al primer elemento de la primera lista
x[0][0]

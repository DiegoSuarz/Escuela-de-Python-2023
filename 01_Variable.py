
#Ejecutar con el inteprete de Python no con la terminal!!!!!!!!!!!!!!
#Operaciones basica con pyton

num1 = 2 + 2  #suma
num1

num2 = 5*6 #multiplicacion
num2

num3 = 50/2 #division, siempre devuelve un valor flotante
num3

num4 = (50 -5*6)/4 #siempre ejecuta primero los parentesis
num4

num5 = 17 // 3  #division entera, devuelte solo el valor entero
num5

num6 = 17 % 3 #Devuelve el modulo o residuo de la division
num6

num7 = 5 ** 2 #Operador para calcular potencia
num7

#Variables:
width = 20
height = 5*9
print(width*height)

tax = 12.5 / 100
price = 100.50
price * tax

#suma = price + _ ## "_" toma el valor de la ultima expresion impresa en la terminal solo funciona al interacctuar con el interprete de python
#print(suma) 

#Tipo de numeros que admite python:
a = 5 #numero decial (int)
b = 3.6 #numero fraccionario (float)
c = 3 + 5j #numero complejo

# Cadenas de carateres
# se puede utilizar '' o ""
'Hola mundo'
"Hola mundo"
'Hola \' mundo'
"Hola ' mundo"
'Hola " Mundo'
"Hola \nMundo"   #nueva linea
"Hola \tMundo"   #tabulador
"hola \rMundo"  #retorno de carro
r'C:\some\name' #imprime directorios de carpetas

""" 
**************************
Operaciones con cadenas
***************************
"""

#####
texto = "hola"
texto*3   #multiplicar cadenas

####
texto+texto #sumar o concatenar cadenas

####
3 * 'un' + 'ium' #multiplicar y concatenar cadenas

####
'Hola' 'Mundo'

####
p = 'Py'
p + 'thon'

####
palabra = "python"
palabra

#acceder a cada letra de la cadena desde el comienzo hasta el final
palabra[0]
palabra[1]
palabra[2]
palabra[3]
palabra[4]
palabra[5]

#acceder a cada letra de la cadena desde el final hasta el comienzo
palabra[-1]
palabra[-2]
palabra[-3]
palabra[-4]
palabra[-5]
palabra[-6]

palabra[0:3] #devuelve el valor de la cadena desde la posicion 0 hasta la posicion 2 (la posicion 3 no la imprime)
palabra[0:2]
palabra[3:]  #desde la posicion 3 hasta el final
palabra[1:3] #desde la posicion 1 hasta el 2
palabra[2:45] #simplemente imprime hasta el fina
palabra[45:] #imprime vacio, ya que desde esta posicion la cadena esta vacia

#las cadena son inmutables
'S' + palabra[1:] #esto no modifica la variable palabra
palabra = 'S' + palabra[1:] #esto si modifica la variable palabra
palabra

####
len(palabra) #nos devuelve la cantidad de carateres que hay un string

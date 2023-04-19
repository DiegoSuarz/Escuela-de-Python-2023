
#Operadores relacionales:
#comparan 2 valores enteros, flotantes o cadenas
####
a = 10
b = 5

a == b
a == a
a != b
a > b
a < b
a >= b
a <= b
4 == 4
2.5 != 3.5
'Hola' == 'Hola'
'Hola' == 'hola'
'Hola' == 'Hola '
'Hola' != 'Hola '

#Operadores logicos:
#comparan 2 tipos de datos booleanos
not True
not False

True and True
True and False
False and True
False and False

True or True
True or False
False or True
False or False

#####
a = 10
b = 5
(a == b) and (a != b)
(a == b) or (a != b)
(a == b) or not(a != b)

####
#Expresiones Anidadas

num1 = 10
num2 = 5

num1 * num2 - 2 ** num2 >= 20 and not(num1 % num2) != 0
num1 * num2 - 2 ** num2 >= 20 or not(num1 % num2) != 0

#####
#Operadores en asignación:
#simplificar orperaciones aritmeticas

c = 10
c = c + 5
c += 5
c -= 5
c *= 5
c /= 5
c //= 5
c %= 5
c **= 5

####
#Operadores de incremento y decremento, se usa con operadores en asignación
c = 0
c += 1
c += 1
c += 1

c -= 1
c -= 1
c -= 1

####
#Opeardore de identidad: Para identificar si es o no es.
#sirve para saber si un objeto es identico al otro objetos (variables)

texto1 = 'hola'
texto2 = 'hola'

texto1 is texto1
texto1 is texto2

texto2 = 'Hola'
texto1 is texto2

texto1 is not texto2

n = 10
m = 10

4 is 4 #salta una advertencia ya que is solo se usa en objetos no en literales

####
#Operadores de pertenencia; es usa en listas, o cadenas, o objetos

texto = 'Hola Mundo'
'h' in texto
'H' in texto
'Hola' in texto

nombres = ['Alex', 'Roel',25]
25 in nombres
'Alex' in nombres
'Juan' in nombres
'Juan' not in nombres

####
#Operaciones con booleanos
type(True)
type(False)

True + True
False * 10
True * 5
True > False
True < False
True == True

c = 0
c += True
c += True
c += True
c

c-= True
c-= True
c

True is True
True is False
True is not True
True is not False

int(True)
int(False)

float(True)
str(True)

bool(1)
bool(34)
bool(0)
bool(-7)
bool(0.5)
bool(0.0)
bool("False")
bool(" ")
bool("")

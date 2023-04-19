### convertir todos las letras en mayusculas
saludo = 'Hola mundo'
saludo.upper() 
saludo

### Convertir todsa las letras en minusculsa
saludo.lower()
saludo

### Hacer la primera letra mayuscula
saludo = 'hola mundo'
saludo.capitalize()
saludo

### hacer mayusculas la primera letra de todas las palabras
saludo.title()

### obtener cuantas veces se repite una caracter dentro de una cadena
saludo.count('o')

### reemplazar una parte de la cadena
palabra = 'Python'
palabra = palabra.replace('P','S')
palabra

'P y t h o n'.replace(' ','')

### borra los espacios en blanco de la extremos de una cadena
'    Hola Mundo'.strip()

'----Hola - Mundo-----'.strip('-')

### Convertir una cadena en una lista:
'Hola Mundo'.split()

'Hola,Mundo,de,python'.split(',')

### Verificar si todos los caracteres de la cadena son minusculas
'Hola'.islower()

'hola'.islower()

### Verificar si todos los caracteres de la cadena son mayusculas
'Hola'.isupper()

'HOLA'.isupper()

### Verificar si todos los caracteres son espacios
'      '.isspace()

'    s  '.isspace()

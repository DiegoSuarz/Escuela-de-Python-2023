print('Hola mundo')

nombre = 'Diego Suarez'
edad = 31

#datos = nombre + edad #no se puede hacer directamente concatenar
datos = nombre ,edad #transformando en una tupla
print(datos)

print(nombre)
print(edad + 1)

""" 
Muestra la información del usuario
por pantalla
"""

print('Nombre:',nombre) #concatenar cadenas
print('Edad',edad)

print(f'Nombre: {nombre}\nEdad: {edad}') #f significa formatear la información

nombre = 'Diego'

def saludar():
    global  apellido_p #permite usar una variable desde afuera de la funcion
    apellido_p = 'Suarez'
    edad = 32
    return 'Hola desde la funcion saludar'
   

#print(saludar())
saludo = saludar()
print(saludo)

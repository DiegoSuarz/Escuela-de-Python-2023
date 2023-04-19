nombre = 'Diego'

def datos():
    global  apellido_p #permite usar una variable desde afuera de la funcion
    apellido_p = 'Suarez'
    edad = 32
    return 'Hola desde la funcion saludar', nombre, edad
   

valores = datos() #devuelve los valore como una tupla
saludo, apellido, edad_ = datos()

print(valores)

print(saludo)
print(apellido)
print(edad_)
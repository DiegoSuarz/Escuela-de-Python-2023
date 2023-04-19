#saludar() #las funciones deben ir antes de llamarse para que se definan correctamente

nombre = 'Diego'

def saludar():
    global  apellido_p #permite usar una variable desde afuera de la funcion
    apellido_p = 'Suarez'
    apellido_m = 'Inocente'
    print('Hola desde la funcion saludar')
    print('hola', nombre)
    print('hola', apellido_p,apellido_m)

saludar()

print('Hola desde fuera de la funcion ',apellido_p)
""" se se quiere enviar varios paramentros o devolver 
    varios valores de una funcion y no se sabe la cantidad
    exacta de los datos se hace lo siguiente:
"""

def sumar(*args, **kwargs):  #*args : argumentos indeterminados por posicion, **kwargs: argumentos indeterminados por nombre
    suma = 0
    for i in args:
        suma += i
    return suma,kwargs


SumaTotal , datos = sumar(1,2,3,4,5,6, nombre = 'Diego', edad = 32)
print('La suma total es: ', SumaTotal)
print(datos)
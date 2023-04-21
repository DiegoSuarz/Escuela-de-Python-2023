

class Persona:
    #(encapsulamiento) atributos privados, solo estan visibles en este archivo, no estan disponible en la funcion main:
    __nombre = None
    __edad = None

    #constructor:
    def __init__(self,nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    #metodo privado:
    def __metodo_privado(self):
        print('Soy un método privado')

    ##medotos publicos para poder obtener el atributo privado nombre
    def get_nombre(self):
        return self.__nombre

    ##medotos publicos para poder modificar el atributos privado nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    ##medotos publicos para poder obtener el atributo privado nombre
    def get_edad(self):
        return self.__edad

    ##medotos publicos para poder modificar el atributos privado nombre
    def set_edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f'Nombre: {self.__nombre} \nEdad: {self.__edad}'
        

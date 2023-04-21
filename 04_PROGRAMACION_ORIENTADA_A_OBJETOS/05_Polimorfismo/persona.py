class Persona():
    def __init__(self, nombre):
        self.nombre = nombre

    def moverse(self):
        print('Ando caminando')

class Atleta(Persona):
    #Polimorfismo se refiere a cualidad que tienen las sub clases de modificar lo metodos, contructor, objetos de la clase padre
    def moverse(self):
        print('Ando Corriendo')

class Ciclista(Persona):
    def moverse(self):
        print('Ando moviendome en mi bicicleta')

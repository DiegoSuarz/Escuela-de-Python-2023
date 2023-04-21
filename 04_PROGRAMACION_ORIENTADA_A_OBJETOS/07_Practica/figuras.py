import math

class Figura(object):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def area(self):
        pass

    def perimetro(self):
        pass

class Rectangulo(Figura): #heredar la clase figura
    #constructor:
    def __init__(self, base, altura):
        self.nombre = __class__.__name__ #redifiniendo el nombre para esta clase rectangulo
        self.base = base
        self.altura = altura

    def area(self):
        return self.base  + self.altura
    
    def perimetro(self):
        return 2 * self.base + 2*self.altura
    
    #redifinir el metodo __str__
    def __str__(self):
        return f'{self.nombre}[base: {self.base} altura: {self.altura}]'


class Circulo(Figura): #Hereda los metodos y atributos de la clase figura:
    def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f'{self.nombre}[radio: {self.radio}]'

def probar_figura(figura): #declaramos un objeto arbitrario que nos va a permitir pasar como argumento una clase
    print(figura)
    print('Area: ', round(figura.area(),2))
    print('Perimetro: ',round(figura.perimetro(),2))
    

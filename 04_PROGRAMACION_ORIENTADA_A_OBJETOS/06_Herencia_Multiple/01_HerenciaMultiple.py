
class A:
    def __init__(self):
        print('Soy Clase A')
    
    def a(self):
        print('Soy método de A')

class B:
    def __init__(self):
        print('Soy Clase B')

    def b(self):
        print('Soy Método de B')

class C(B,A): #herencia multiple se esta heredando los metodos de la clase A y clase B, y se le da mas importancia a la calse que se defien a la izquierda en este caso a la calse B
    def c(self):
        print('Soy método de C')

#desde la clase c se hereda la clasa B y la clase A
c1 = C() #imprime en pantalla "soy de clase B", ya que la clase C no tiene un contrustor y hereda el contructor de la clase que tiene mayor prioridad, en este caso la calse B

c1.a()
c1.b()
c1.c()

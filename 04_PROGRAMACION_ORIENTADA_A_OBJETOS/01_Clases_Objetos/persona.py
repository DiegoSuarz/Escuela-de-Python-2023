
class Persona: #crear una clase
    
    # #atributos de la clase persona (variables)
    #Ya no son necesarios ya que usamos el contrustor para definir los objetos
    # nombre = None
    # edad = None
    
    #constructor sirve para simplificar el llamado de objetos:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Metodos: comportamientos de los objetos (acciones) (funciones)
    def mostrar_datos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ',self.edad)

    def __str__(self) -> str: #este metodo sirve para mostrar el valor de los objetos mediante la funcion print 
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'
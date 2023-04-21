
###Super clase o clase padre:
class Persona:
    #constructor
    def __init__(self,nombre,edad):
        #atributos:
        self.nombre = nombre
        self.edad = edad

    #metodo:
    def detalle_persona(self):
        print(f'Nombre {self.nombre} \nEdad: {self.edad}')


    def __str__(self):
        return f'Nombre {self.nombre} \nEdad: {self.edad}'
    
### Herencia:
#sub clase Cliente
class Cliente(Persona): #La sub clase cliente va a Heredar los atributos de la clase persona 
    pass

#sub clase Empleado que hereda los atributos de la clase persona
class Empleado(Persona):
    #constructor de la clase empleado
    def __init__(self, nombre, edad, sueldo):
        
        #para agregar un atributo a la clase padre se usa la funcon super
        
        Persona.__init__(self, nombre, edad) #heredar el constructor de la clase persona
        self.sueldo = sueldo

    def detalle_empleado(self):
        Persona.detalle_persona(self) #Heredar el metodo detalle_persona, de la clase padre
        print('Sueldo:',self.sueldo)

    def __str__(self):
        return Persona.__str__(self) + f'\nSueldo: {self.sueldo}' #Heredad el metodo de la clse persona y concatenar el dato que falta

 
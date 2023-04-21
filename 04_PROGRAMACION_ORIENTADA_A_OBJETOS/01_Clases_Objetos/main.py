from persona import Persona

####Sin constructor
# persona1 = Persona() #al asignarle una clase a una variable se transforma en objeto (instancia)
# persona1.nombre = 'Alex'
# persona1.edad = 32

# persona2 = Persona() #al asignarle una clase a una variable se transforma en objeto (instancia)
# persona2.nombre = 'Diego'
# persona2.edad = 26

# persona1.mostrar_datos()
# print('='*20)
# persona2.mostrar_datos()


#####un constructor es que que construye un objeto y sirve al momento de crear un objeto
#con constructor

persona1 = Persona('Alex',32)
persona2 = Persona('Diego',25)
persona1.mostrar_datos()
persona2.mostrar_datos()

persona1.nombre = 'Roberto'
persona1.mostrar_datos()
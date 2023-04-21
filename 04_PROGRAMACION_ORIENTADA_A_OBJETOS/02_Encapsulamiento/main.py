
from persona import Persona

persona1 = Persona('Alex',35)

#modificar el atributo privado "nombre" del objeto persona1
persona1.set_nombre('Roberto')

#imprimor en pantalla el atributo privado "nombre"
print(persona1.get_nombre())
print(persona1)
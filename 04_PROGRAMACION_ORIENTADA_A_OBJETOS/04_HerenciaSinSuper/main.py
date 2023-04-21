
from persona import Cliente, Empleado


cliente1 = Cliente('Roberto',35)
cliente2 = Cliente('Alex',34)

cliente1.detalle_persona()

print(cliente2)

empleado1 = Empleado('Alex',25,2355)
empleado2 = Empleado('Roel',26,2833)

empleado1.detalle_persona()
empleado1.detalle_empleado()

print(empleado2)
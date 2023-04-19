
datos = ['Alex',25,'Perú']

###agrega un miembro a la lista
datos.append('Roel') 
datos

###Extiende la lista agregándole todos los ítems del iterable. Equivale a a[len(a):] = iterable.
datos.extend(datos)
datos

###insertar un elemento en una posicion especifica
datos.insert(2,'Agregado')
datos

###remove: quitar un elemento de la lista
datos.remove('Alex')
datos

###pop: Eliminar el ultimo elemento de la lista
datos.pop()
datos

###clear: Elimina todos los elementos de una lista
datos.clear()
datos

####
datos = ['Alex',25,'Perú','Roel']
###index:  devuele al posicion o indice donde se encuentra un elemento del arregle:
datos.index('Perú')

 ###count: contabiliza cuanta veces se repite un elemento de la lista
datos = ['Alex',25,'Perú','Roel',150,150,150]
datos.count(150)

###sort: ordena la lista alfabeticamente
frutas = ['naranja','pera','manzana','uva','aguacate']
frutas.sort()
frutas

###reverse: invierte la lista de datos:
numeros= [1,2,3,4,5,6]
numeros.reverse()
numeros

###copy: retorna una copia de una lista
data = numeros.copy()
data

###instruccion del sirve para quitar un elemento de la list, quitar secciones o vaciar la lista entera

a = [1, 2, 3, 4, 5, 6, 7]

del a[0]
a

del a[2:4]
a

del a[:]
a

del a
a
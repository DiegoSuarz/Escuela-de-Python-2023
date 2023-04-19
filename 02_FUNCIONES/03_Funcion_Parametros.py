

def saludar(nombre):
    
    return f'Hola {nombre} desde la funcion saludar'

def sumar(a,b):
    return a + b

def restar(c,d):
    return c - d

def multiplicar(e=None,f=None):
    if e == None or f== None:
        print('Error: debes enviar dor números a la función')
        return
    return e * f

saludo = saludar('Diego')
print(saludo)

suma = sumar(4,3)
print('La suma es: ',suma)

resta = restar(c = 20, d = 40)
print('La resta es: ', resta)

multiplica = multiplicar()
print('La multiplicación es: ', multiplica)



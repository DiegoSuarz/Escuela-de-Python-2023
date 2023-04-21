def dividir(a,b):
    if b == 0:
        #lanzar una excepcion de manera directa:
        raise ZeroDivisionError('Error: no se puede dividir por cero!')
    else:
        return a/b
    

dividir(4,0)
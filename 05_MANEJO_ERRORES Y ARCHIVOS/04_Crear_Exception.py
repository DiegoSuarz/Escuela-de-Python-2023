class OperadorExcepection(Exception): #heredar los metodos de la clase Exception
    #constructor:
    def __init__(self,mensaje):
        super().__init__(mensaje)

    
    




def dividir(a,b):
    if b == 0:
        #lanzar una excepcion de manera directa:
        raise OperadorExcepection('Error: no se puede dividir por cero!')
    else:
        return a/b
    

dividir(4,0)
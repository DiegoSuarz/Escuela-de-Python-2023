"""
Crear un sistema que detecte si un numero es 
primo o no ( el numero primo se debe dar una 
division exacta solo 2 veces, con 1 y con sigo 
mismo)
"""

def es_primo(numero):
    contador = 0
    
    for i in range(1, numero+1):
        if i == 1  or i == numero:
            continue
        if numero % i == 0:
            contador  += 1
    
    if contador == 0:
        return True
    else:
        return False


def main():
    numero = int(input('Ingrese un numero: '))
    if es_primo(numero):
        print('Es primo')
    
    else:
        print('No es primo')


if __name__ == '__main__': #desde aqui empezara a ejecutarse el codigo
    main()
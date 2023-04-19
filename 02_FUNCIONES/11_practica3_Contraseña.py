"""
Crear un sistema que genere
una contraseña aleatoria
"""

import random

def generarPass():
    mayusculas = ['A','B','C','D','E']
    minusculas = ['a','b','c','d','e']
    simbolos = ['#','$','%','&']
    numeros = ['1','2','3','4','5','6','7']

    caracteres = mayusculas + minusculas + simbolos + numeros
    password = []

    for i in range(15):
        carater_random = random.choice(caracteres) #selecciona un caracter random de una lista
        password.append(carater_random)

    password = "".join(password) #convierte en una string cada una de los carateres generados aleatoriante
    return password

def main():
    key = generarPass()
    print('Tu nueva contraseña es: ', key)

if __name__ == '__main__':
    main()
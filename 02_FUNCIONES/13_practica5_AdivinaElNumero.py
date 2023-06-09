"""Crear un juego donde el sistema genere
un numero aleatorio y el jugador intente
adivinar el numero aleatorio"""

import random

def jugar(vidas):
    numero_random = random.randint(1,100)
    numero_elegido = None #variable vacia

    while numero_random != numero_elegido:
        numero_elegido = int(input("Ingrese un número entre 1 y 100: "))

        if numero_random < numero_elegido:
            print("Elige un número más pequeño")
            vidas -= 1
        elif numero_random > numero_elegido:
            print("Elige un número más grande")
            vidas -= 1

        if vidas == 0:
            print("GAME OVER")
            break

        print(f'Te quedan {vidas} vidas')
    
    if numero_elegido == numero_random:
        print("FELICIDADES GANASTE EL JUEGO")   

def main():
    while True:
        menu = """
        ADIVINA EL NUMERO ALEATORIO
        1 - Nivel Facil
        2 - Nivel Intermedio
        3 - Nivel Dificil
        4 - Salir

        Ingrese una opcion: """

        opcion = input(menu)

        if opcion == '1':
            jugar(10)
        elif opcion == '2':
            jugar(7)
        elif opcion == '3':
            jugar(5)
        elif opcion == '4':
            print("CERRANDO JUEGO")
            break
        else:
            print("Opcion incorrecta vuelve ingresar")

        


if __name__ == '__main__':
    main()

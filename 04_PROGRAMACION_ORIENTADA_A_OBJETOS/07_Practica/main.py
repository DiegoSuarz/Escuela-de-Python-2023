"""
1. rear un módulo figuras.py, y dentro crea clases como Figura, Rectangulo, Circulo y la función probar_figura.
2.  Crear una clase Figura, con atributo nombre. Crear también el constructor de la clase y los métodos necesarios área y el perímetro con instrucción pass.
3. Crear otra clase Rectángulo que herede de la clase Figura, con atributos base y altura. Crear también el constructor de la clase y reescribe los métodos de la clase Figura para calcular el área y el perímetro.
4. Crear otra clase Circulo que herede de la clase Figura, con atributo radio. Crear también el constructor de la clase y reescribe los métodos de la clase Figura para calcular el área y el perímetro.
5. Crear una función probar_figura donde reciba un objeto para probar diferentes figuras como rectángulo o circulo. Y imprima el estado del objeto y como también el área y perímetro.
6. Crear un módulo principal main.py, luego importa desde el modulo figuras las clases Rectángulo, Circulo y la función probar_figura.
7. Crear la función principal que puede ser main() y el punto de entrada de la aplicación de Python y llama a ejecutar la función main().
8. Dentro de la función main() crea un sistema que tenga un bucle infinito y también tenga un menú de navegación donde las opciones sean 1-Rectangurlo 2-Circulo 4-Salir
9. En la opción 1 pide al usuario que ingrese base y altura del rectángulo y crea un objeto de rectángulo y ese objeto envía al funcion probar_figura()
10. En la opción 2 pide al usuario que ingrese el radio del circulo y crea un objeto de circulo y ese objeto envía al función probar_figura()
11. En la opción 3 termina el bucle infinito y se cierra el programa.
"""

from figuras import Rectangulo, Circulo, probar_figura

def main():
    while True:
        menu = """
        AREA  Y PERIMETRO DE FIGURAS GEOMETRICAS:
        
        1 - Rectangulo
        2 - Circulo
        3 - Salir
        Ingrese una opción: """

        opcion = input(menu)
        if opcion == '1':
            base = float(input('Ingrese Base: '))
            altura =float(input('Ingrese Altura: '))
            r = Rectangulo(base , altura)
            probar_figura(r)

        elif opcion == '2':
            radio = float(input('Ingrese Radio: '))
            c = Circulo(radio)
            probar_figura(c)

        elif opcion == '3':
            print('Cerrando sistema')
            break
        
        else:
            print('Opción incorrecta')



if __name__ == '__main__':
    main()
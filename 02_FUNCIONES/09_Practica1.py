""" 
Crear un sistema que detecte si una palabra
es palíndroma o no
"""

def palindromo(palabra):
    palabra = palabra.replace(' ','') #borrar los espacios
    palabra = palabra.lower() #poner todas las palabras en minuscula

    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


#funcion principal
def main():

    palabra = input('Ingrese una palabra: ')

    es_palidromo = palindromo(palabra)
    
    if es_palidromo:
        print('la palabra es Palindromo')
    else:
        print('La palabra no es palindromo')
    

#punto de entrada de la aplicacion
if __name__ == '__main__': #desde aqui empezara a ejecutarse el codigo
    main()
from io import open
from os import path

def escribir_archivo():
    archivo = open('texto.txt','w') #abrir un archivo, si no esta creado crealo, modo escritura
    archivo.write('Hola mundo de Python')
    archivo.close()


def leer_archivo():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt','r')
        #textos = archivo.read() #solo muesra en el teminal el contenido del archivo
        textos = archivo.readlines() #genera un lista para cada archivo
        archivo.close()
        print(textos)


#escribir_archivo()
leer_archivo()
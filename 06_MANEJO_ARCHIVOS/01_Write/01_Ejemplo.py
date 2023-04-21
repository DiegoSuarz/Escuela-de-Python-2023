from io import open

def escribir_archivo():
    archivo = open('texto.txt','w') #abrir un archivo, si no esta creado crealo, modo escritura
    archivo.write('Hola mundo de Python')
    archivo.close()


escribir_archivo()
from sys import argv

if len(argv) == 3:
    nombre = argv[0]
    edad = int(argv[1])
    altura = float(argv[2])

    #print(f'Nombre: {nombre} \nEdad: {edad}\nAltura: {altura}')
    #print('nombre: {} \nEdad: {}Altura: {}'.format(nombre, edad, altura))
    #print('nombre: {a} \nEdad: {b}Altura: {c}'.format(a=nombre, b=edad, c=altura))
    print('nombre: %s \nEdad: %i \nAltura: %f'%(nombre, edad, altura))

# else:
#     print('Error, Ingrese los argumentos correctamente')
#     print('Ejemplo: formateo.py "Nombre" 25 1.67')

# import sys
# sys.path.append('/ufs/guido/lib/python')
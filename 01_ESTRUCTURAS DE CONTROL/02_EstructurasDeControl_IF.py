#if

# if True:
#     print("Se cumple la condicion")

# if False:
#     print("Se cumple la condicion")

# 
# if False:
#     print("Se cumple la condicion")
# else:
#     print("No se cumplio la condicion")

# ##############

# n = int(input('Ingrese un número entero: '))

# if n % 2 == 0:
#     print(f'En numero {n} es PAR')
# else:
#     print(f'En número {n} es IMPAR')

###### anidaddo
n = int(input('Ingrese un número entero: '))

if n != 0:
    if n > 0:
        if n % 2 == 0:
            print(f'El número {n} es PAR POSITIVO')
        else:
            print(f'El número {n} es IMPAR POSITIVO')

    else:
        if n % 2 == 0:
            print(f'El número {n} es PAR NEGATIVO')
        else:
            print(f'El número {n} es IMPAR NEGATIVO')

else:
    print(f'El número {n} es NEUTRO')
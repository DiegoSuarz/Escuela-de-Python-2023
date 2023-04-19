
sumar = lambda a, b: a+b

duplicar = lambda n: n*2

par = lambda n: n % 2 == 0
impar = lambda n: n % 2 != 0

revertir = lambda cadena: cadena[::-1]

print(sumar(10,20))
print(duplicar(10))

print(par(6))
print(par(3))

print(impar(6))
print(impar(3))

print(revertir('Hola'))

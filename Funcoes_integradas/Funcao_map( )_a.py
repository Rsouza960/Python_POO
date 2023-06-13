lista = [1,2,3,-4,5]
lista2 = [11,12,13,14,15]
r = map(abs, lista)
cubo = map(lambda x: x*x*x, lista)
# print(list(cubo))

soma = map(lambda x, y: x+y, lista, lista2)
print(list(soma))

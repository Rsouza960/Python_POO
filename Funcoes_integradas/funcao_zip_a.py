lista = [1,2,3,4,5]

tupla = (10,11,12,13,14,15)

dicionario= {'a': 21, 'b': 22, 'c': 23, 'd': 24}
r = zip(lista, tupla, dicionario.values())
print(list(r))
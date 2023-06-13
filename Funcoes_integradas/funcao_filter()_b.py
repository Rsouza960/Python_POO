lista = [
    {'nome':'Jose', 'idade': 28},
    {'nome':'Adriana', 'idade': 39},
    {'nome':'Pedro', 'idade': 17},
    {'nome':'Maria', 'idade': 23},
    {'nome': 'Roberto', 'idade': 15},
]

menores = filter(lambda p: p['idade']<18, lista)
print(list(menores))


nomes = filter(lambda p: len(p['nome']) < 6, lista)
print(list(nomes))
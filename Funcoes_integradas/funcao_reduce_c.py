from functools import reduce

pessoas = [
    {'nome':'Jose', 'idade': 28},
    {'nome':'Adriana', 'idade': 16},
    {'nome':'Pedro', 'idade': 50},
    {'nome':'Maria', 'idade': 23},
    {'nome':'Ronny', 'idade': 14},
]

idades = map(lambda p: p['idade'], pessoas)
so_menores = filter(lambda idade: idade < 18, idades)


soma_menores = reduce(lambda a, b: a + b, so_menores, )
print(f'Soma das idades menores que 18 é {soma_menores}')
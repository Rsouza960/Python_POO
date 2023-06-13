v1 = [1200, 234, 2345, 1560]
v2 = [1245, 300, 2103, 1434]
p = ['Fogao', 'Liquidificador', 'Geladeira', 'TV']

lista = {venda[0]: max(venda[1], venda[2]) for venda in zip(p, v1, v2)}
print(lista)
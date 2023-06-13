produtos = [('tv', 2500), ('fogao', 1240), ('radio', 234)]

novo_preco = lambda produto: (produto[0], produto[1] * 1.05)

print(list(map(novo_preco, produtos)))
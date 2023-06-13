def quadrado(x):
    return lambda: x * x

funcoes = [quadrado(i) for i in [1,2,3,4,5]]

for funcao in funcoes:
    print(funcao())
nomes = ['Adriana', 'Ronny', 'Rene', 'Marcelo', 'Tereza']



print(min(nomes))
print(max(nomes))


print(min(nomes, key=lambda nome: len(nome)))
print(max(nomes, key=lambda nome: len(nome)))
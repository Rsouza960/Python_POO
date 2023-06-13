''' __repr__ (mostra a representação do elemento.)

podemos sobrescreve-lo de uma forma mais adequada aos nossos interesses.

  '''


class Livro:
    def __init__(self, titulo, autor, editora, ano):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
    def __repr__(self):
        return f'{self.titulo} - {self.autor}'

livro1 = Livro('Algoritmos e programação de computadores', 
               'Piva Jr, et al',
                'Elsevier',
                2019
)

livro2 = Livro('Estrutura de Dados Técnicas de programação',
                'Piva Jr, et al',
                'Elsevier',
                2014
)

print('\nESSES SÃO EXEMPLOS "__repr__"')
print(livro1)
print(livro2)
print()

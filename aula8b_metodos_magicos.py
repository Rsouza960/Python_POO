'''
__str__ - Mostra uma string predefinida do elemento.

O padrão de exibição de __str__, é chamar (imprimir) __repr__

'''

class Livro:
    def __init__(self, titulo, autor, editora, ano):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano


    def __repr__(self):
        return f'{self.titulo} - {self.autor}'
    

    def __str__(self):
        return f'{self.ano} - {self.titulo}'

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

print('\nESSES SÃO EXEMPLOS "__str__"')
print(livro1)
print(livro2)
print()
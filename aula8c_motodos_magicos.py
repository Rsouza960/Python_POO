'''
__len__ Mostra o tamanho de um elemento.
Ao sobreescrever, nos definimos
o que será levado em conta para retornar o tamanho.
'''

class Livro:
    def __init__(self, titulo, autor, editora, ano, paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.paginas = paginas


    def __repr__(self):
        return f'{self.titulo} - {self.autor}'
    

    def __str__(self):
        return f'{self.ano} - {self.titulo}'
    
    def __len__(self):
        return self.paginas

livro1 = Livro('Algoritmos e programação de computadores', 
               'Piva Jr, et al',
                'Elsevier',
                2019,
                472
)

livro2 = Livro('Estrutura de Dados Técnicas de programação',
                'Piva Jr, et al',
                'Elsevier',
                2014,
                508
)


print(livro1)
print(livro2)

print(len(livro1))
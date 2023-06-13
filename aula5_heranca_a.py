class Mamifero:
    def __init__(self, pelo, mamas, idade):
        self.__pelo = pelo
        self.__mamas = mamas
        self.__idade = idade

    def comunicar(self):
        ...

    
class Cachorro(Mamifero):
    def __init__(self, pelo, mamas, idade, rabo):
        Mamifero.__init__(pelo, mamas, idade)
        self.__rabo = rabo
        
    def cor_rabo(self):
        print(f'o cachorro tem o rabo cor{self.__rabo}')
    
    def latir(self):
        ...


class Gato(Mamifero):
    def __init__(self, pelo, mamas, idade, rabo):
        super.__init__(pelo, mamas, idade)
        self.__rabo = rabo

    def miar(self):
        ...


cachorro = Cachorro('caramelo', 'mamas', 7)
cachorro.cor_rabo()




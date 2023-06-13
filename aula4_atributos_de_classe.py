class Automovel:
    contador = 0
    precisao = 0.95

    def __init__(self, placa, velocidade_max):
        self.__id = Automovel.contador + 1
        self.__placa = placa
        self.__velocidade_max = velocidade_max * Automovel.precisao
        self.__velocidade_atual = 0
        Automovel.contador = self.__id

    def __str__(self):
        return f'{self.__id} - {self.__velocidade_atual} Km/h'

    def get_placa(self):
        return self.__placa
    
    def get_velocidade_maxima(self):
        return self.__velocidade_max
    
    def set_velocidade_max(self, nova):
        self.__velocidade_max = nova
        print(f'A nova velocidade maxima é: {nova}Km/h')
    

    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} Km/h')
        

    def acelerar(self):
        maxima = self.__velocidade_max
        nova = self.__velocidade_atual + 10
        if self.__velocidade_atual == 180:
            print('alcancou velocidade maxima')
        self.velocidade_atual = nova if nova <=maxima else maxima
        
        

    def frear(self):
        print(f'Freando....')
        nova = self.__velocidade_atual - 10
        self.__velocidade_atual = nova if nova >= 0 else 0
        

meu_carro = Automovel('XY0011', 180)
outro_carro = Automovel('ZZZ0000', 200)

print(meu_carro)
print(meu_carro.get_velocidade_maxima())
print(meu_carro.get_placa())

print(outro_carro)
print(outro_carro.get_velocidade_maxima())
print(outro_carro.get_placa())





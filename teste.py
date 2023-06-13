class Smartphone:
    def __init__(self, modelo, cor, memoria, system):
        self.__modelo = modelo
        self.__cor = cor
        self.__memoria = memoria
        self.__system = system

    def get_modelo(self):
        return self.__modelo
    
    def get_cor(self):
        return self.__cor
    
    def get_memoria(self):
        return self.__memoria
    
    def get_system(self):
        return self.__system
        
    
    def toque(self):
        print('está tocando musica')


class Android(Smartphone):
    def __init__(self, modelo, cor, memoria, system = 'Android'):
        super().__init__(modelo, cor, memoria, system)

    def toque(self):
        print (f'está tocando a musica do samsung')
            
    
class Iphone(Smartphone):
    def __init__(self, modelo, cor, memoria, system):
        super().__init__(modelo, cor, memoria, system)

    def toque(self):
        print (f'está tocando a musica do iphone')

    

    
    
android= Android('Samsung', 'preto', '128 gb', 'android')
iphone = Iphone('iphone12', 'prata', '256 gb', 'ios')


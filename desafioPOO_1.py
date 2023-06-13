from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email=email
        self.__senha = cryp.hash(senha, rounds=1000, salt_size = 10)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
while True:
    nome = input("nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    conf_senha = input("Confirme a senha: ")

    if senha == conf_senha:
        user = Usuario(nome, sobrenome, email, senha)
        break
    else:
        print('As senhas não conferem! ')

print('Usuario criado com sucesso!!')

senha = input('informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')
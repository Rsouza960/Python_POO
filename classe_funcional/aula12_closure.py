def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular

dobro = multiplicar(2)
triplo = multiplicar(3)


print(f'O dobro de 4 é {dobro(4)}')
print(f'o triplo de 5 é {triplo(5)}')
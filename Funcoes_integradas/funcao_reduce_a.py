from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]

r = reduce(lambda x, y: x+y, lista, 1000)
print(r)
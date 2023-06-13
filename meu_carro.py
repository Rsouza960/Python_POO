from carro import Carro 
from datetime import datetime

carro_novo = Carro('Corolla', 2022)

print(carro_novo.get_descricao())
carro_novo.set_odometro(345)
print(carro_novo.get_kilometragem())
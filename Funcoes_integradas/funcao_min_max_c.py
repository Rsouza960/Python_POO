musicas = [
    {'titulo': 'Amigo', 'tocou': 4},
    {'titulo': 'ai se eu te pego', 'tocou': 45},
    {'titulo': 'Para sempre', 'tocou': 12},
    {'titulo': 'Nuvem de Lagrimas', 'tocou': 23},
    {'titulo': 'Papel Manchê', 'tocou': 14},
]

print(min(musicas, key= lambda musica: musica['tocou']))
print(max(musicas, key= lambda musica: musica['tocou']))


musicas = [
    {'titulo': 'Amigo', 'tocou': 4},
    {'titulo': 'ai se eu te pego', 'tocou': 45},
    {'titulo': 'Para sempre', 'tocou': 12},
    {'titulo': 'Nuvem de Lagrimas', 'tocou': 23},
    {'titulo': 'Papel Manchê', 'tocou': 14},
]

#ordenacao da mais tocada

print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
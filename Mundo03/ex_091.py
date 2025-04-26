from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
print('Valores sorteados!')
rank = []
for c, v in jogo.items():
    print(f'O {c} jogou {v}')
    sleep(1)
print('-----RANKING-----')
rank = sorted(jogo.items(), key= itemgetter(1), reverse= True)
for i, v in enumerate(rank):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    
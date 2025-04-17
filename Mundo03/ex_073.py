brasileirao = ('Flamengo', 'Palmeiras', 'Fluminense', 'Ceará', 'Bragantino', 'Vasco da Gama',
            'Juventude', 'Mirassol', 'Internacional', 'Botafogo', 'Fortaleza', 'Santos',
              'Corinthians', 'Vitória', 'Cruzeiro', 'São Paulo', 'Grêmio', 'Bahia', 
              'Atlético-MG', 'Sport')
print('=-' * 100)
print(f'Lista de times do brasileirão 2025.1: {brasileirao}')
print('=-' * 100)
print(f'Lista dos 5 primeiros times: {brasileirao[0:5]}')
print('=-' * 100)
print(f'Lista dos 4 Últimos: {brasileirao[-4:]}')
print('=-' * 100)
print(f'lista em ordem alfabética: {sorted(brasileirao)}')
posicao = brasileirao.index('Botafogo') + 1
print(f'O Botafogo está na posição {posicao}')

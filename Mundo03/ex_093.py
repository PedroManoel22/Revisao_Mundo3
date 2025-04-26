dados = {}
partida = []
dados['jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
cont = 1
soma = 0
while cont <= partidas:
    partida.append(int(input(f'   Quantos gols na {cont}° partida? ')))
    cont += 1
dados['gols'] = partida[:]
dados['total'] = sum(partida)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["jogador"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'   -> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')

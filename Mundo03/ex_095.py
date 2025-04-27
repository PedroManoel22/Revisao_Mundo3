lista = {'gols': list()}
gol = 0
total = 0
i = 1
time = list()
partidas = list()
while True:
    lista.clear()
    lista['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {lista["nome"]} jogou? '))
    partidas.clear()
    for i in range(1, tot+1):
         partidas.append(int(input(f'Quantos gols na {i}° partida: ')))
    lista['gols'] = partidas[:]
    lista['total'] = sum(partidas)
    time.append(lista.copy())
    while True:
        r = str(input('Deseja continuar ? [S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO, Digite apenas S OU N !')
    if r in 'N':
        break
print('-=' * 40)
print(lista)
print('-=' * 40)
print(f'Cod:', end="")
for i in lista.keys():
    print(f'{i:<15}', end="")
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    x = int(input('Mostrar dados de qual jogador ? (999, para cancelar)'))
    if x == 999:
        break
    if x >= len(time):
        print(f'ERRO! o jogador com o código {x} não existe! ')
    else:
        print(f'Levantamento do jogador {time[x]["nome"]}:')
        for i, g in enumerate(time[x]['gols']):
            print(f'   no jogo {i+1} fez {g} gols!')
print('=-' * 40)
print('Finalizado!')

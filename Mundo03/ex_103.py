def ficha(jog='<desconhecido>',gol=0):
    print(f'o jogador {jog} fez {gol} gol(s) no campeonato')


n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

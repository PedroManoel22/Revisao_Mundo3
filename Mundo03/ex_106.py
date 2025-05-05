def ajuda(com):
    help(com)
def titulo(msg):

    tam = len(msg) + 4
    print('\033[1;30;41m~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print('\033[m')
while True:
    titulo('Sistema de Ajuda PyHELP')
    comando = str(input('Função ou biblioteca -> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo')

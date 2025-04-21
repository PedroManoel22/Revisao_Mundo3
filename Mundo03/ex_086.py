matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range(0, 3):
    for z in range(0, 3):
        matriz[i][z] = int(input(f'Insira o valor [{i}{z}] da matriz: '))
for i in range(0, 3):
    for z in range(0, 3):
        print(f'[{matriz[i][z]:^5}]', end='')
    print()

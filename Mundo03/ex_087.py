matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0] ]
pares = 0
terceira_coluna = maior = menor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]       
print('-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
print('-=' * 15)
print(f'A soma dos valores pares é {pares}.')
for l in range(0, 3):
    if matriz[l][2]:
        terceira_coluna += matriz[l][2]    
print(f'A soma dos valores da terceira coluna é {terceira_coluna}.')
for c in range(0, 3):
    if c == 0:
        maior = menor = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
        elif matriz[1][c] < menor:
            menor =  matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')

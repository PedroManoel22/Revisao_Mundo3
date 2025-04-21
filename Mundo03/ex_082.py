lista = []
impares = []
pares = []
while True:
    valores = int(input('Insira um valor: '))
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    lista.append(valores)
    if resp == 'N':
        break
print('-=' * 15)
print(f'A lista completa é: {lista}')
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
print(f'A lista de números pares é: {pares}')
print(f'A lista de números ímpares é: {impares}')

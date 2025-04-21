lista = []
pessoas = []
pesado = 0
leve = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesado = leve = lista[1]
    else:
        if lista[1] > pesado:
            pesado = lista[1]    
        elif lista[1] < leve:
            leve = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    resp = str(input('deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(pessoas)      
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {pesado}. Peso de', end=' ')
for p in pessoas:
    if p[1] == pesado:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {leve}. Peso de', end=' ')
for p in pessoas:
    if p[1] == leve:
        print(f'{p[0]}', end=' ')
    
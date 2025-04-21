lista = [[], []]
for i in range(1, 8):
    valores = int(input(f'Digite o {i}° valor: '))
    if valores % 2 == 0:
        lista[0].append(valores)
    else:
        lista[1].append(valores)
print(f'Lista de pares: {lista[0]}')
print(f'Lista de ímpares: {lista[1]}')

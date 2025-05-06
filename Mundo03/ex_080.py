lista = []
cont = 0
while True:
    valor = int(input('Insira um valor: ')) 
    if cont == 0:
        lista.append(valor)
        print(f'Valor {valor} adicionado no final da lista')
    elif valor > lista[-1]:
        lista.append(valor)
        print(f'valor {valor} adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'valor {valor} adicionado na posição {pos} da lista')
                break
            pos += 1
    cont += 1
    if cont == 5:
        break
print(f'Os números em ordem são: {lista}')

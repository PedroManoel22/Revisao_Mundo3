lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    elif valor in lista:
       print('Número duplicado, não irei adiciona-lo...')
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 15)
print(f'Você adicionou os valores: {sorted(lista)}')
print('Fim do programa. Obrigado. Volte Sempre!')

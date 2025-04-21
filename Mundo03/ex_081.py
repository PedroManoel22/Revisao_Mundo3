lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp =='N':
        break
print('=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
        
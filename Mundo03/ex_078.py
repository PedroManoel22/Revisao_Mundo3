lista = []
for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))          
print(f'você digitou os valores {lista}')
print(f'O maior valor foi {max(lista)}, na posição ', end='')
for i,v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {min(lista)}, na posição ', end='')
for i,v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...',end='')
print()

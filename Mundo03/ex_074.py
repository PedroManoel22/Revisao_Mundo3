from random import randint
lista = (randint(1, 10), randint(1,10),randint(1, 10), randint(1,10), randint(1,10) )
print(f'Os números gerados foram:', end=' ')
for i in range (0, len(lista)):
    print(lista[i], end=' ')
print()
print(f'O menor valor é {min(lista)}')
print(f'O maior valor é {max(lista)}')

from random import randint
from time import sleep
lista = []
total = 1
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
while total <= jogos:
    cont = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    print(f'Jogo {total}: {f"{lista}":^2}')
    sleep(1)
    cont += 1
    lista.clear()
    total += 1
print(f'{"--->":<2}', end='')
print(f' {"BOA SORTE!"} ',end='')
print('<---')
 
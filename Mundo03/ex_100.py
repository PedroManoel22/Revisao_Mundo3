from random import randint
lista = []
def sortear():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0,6):
        lista.append(randint(0,10))
    for i in lista:
        print(f'{i}, ', end='')
    print('Pronto!')
def somando(x):
    soma = 0
    print(f'Somando os valores pares de {x}, temos ', end='')
    for i in x:
        if i % 2 == 0:
            soma += i
    print(soma)
    
sortear()
somando(lista)

lista = ('Caderno', 25.90,
         'Livro', 15.85,
         'Mochila', 90.99,
         'Mouse', 60,
         'Teclado', 99.99,
         'Chinelo', 35.99,
         'Borracha', 2)
print('-' * 40)
print(f'{"Listagem de Preço":^40}')
print('-' * 40)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)

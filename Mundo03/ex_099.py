def analizador(*x):
    print('-=' * 20)
    print('Analizando os valores passados...')
    if x:
        for i in range(0, len(x)):
            print(f'{x[i]} ', end='')
        print(f'foram informados {len(x)} valores ao todo.', end='')
        print()
        print(f'O maior valor informado foi {max(x)}')
    else:
        print('Nenhum valor foi informado')


analizador(2,9,4,5,7,1)
analizador(4,7,0)
analizador(1,2)
analizador(6)
analizador()
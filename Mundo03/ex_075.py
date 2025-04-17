numeros = (int(input('Insira um número: ')), int(input('Insira outro número: ')), int(input('insira mais um número: ')), int(input('Insira o último número: ')))
print(f'Você digitou os seguintes números: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'o valor 3 apareceu na {numeros.index(3)+1}ª posição')
print('Os números pares digitados foram: ', end=' ')
for i in numeros:
    if i % 2 == 0:
        print(i , end=' ')
        
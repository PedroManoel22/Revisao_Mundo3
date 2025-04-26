dados = {}
lista_mulheres = []
pessoas = 0
soma_idade = 0
lista = []
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: ')).upper().strip()[0]
    if dados['sexo'] == 'F':
        lista_mulheres.append(dados['Nome'])
    pessoas += 1
    while dados['sexo'] not in 'FM':
        print('ERRO! Digite apenas F ou M!')
        dados['sexo'] = str(input('Sexo:')).upper().strip()[0]
    dados['idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    soma_idade += dados['idade']
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('A) ', end='')
print(f'Ao todo temos {pessoas} pessoas cadastradas')
print('B) ', end='')
print(f'A média de idade é {soma_idade/pessoas:.2f}')
print('C) ', end='')
print('As mulheres cadastradas foram ',end='')
for i,v in enumerate(lista_mulheres):
    print(f'{v} ', end='')
print()
print('D) ',end='')
print('Lista das pessoas acima da média: ')
for p in lista:
    if p['idade'] >= soma_idade/pessoas:
        for k, v in p.items():
            print(f'{k} = {v}')
        print()

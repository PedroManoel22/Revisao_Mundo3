def leiaInt(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isnumeric():
            return int(valor)
        else:
            print('Erro!')
            mensagem = 'Digite um número: '

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

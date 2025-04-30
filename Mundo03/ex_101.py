
def voto(y):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - y
    print(f'Com {idade}: ', end='')
    if idade < 16:
        print('NÂO VOTA!')
    elif idade >= 18 and idade <= 70:
        print('VOTO OBRIGATÓRIO')
    elif idade < 18 and idade <= 18 or idade > 70:
        print('OPCIONAL')   
x = int(input('Ano de nascimento: '))
voto(x)

from datetime import date
ano_atual = date.today().year
dados = {}
dados['nome'] = str(input('Nome:' ))
dados['idade'] =  ano_atual - int(input('Ano de nascimento: '))
dados['carteira'] = int(input(f'{dados["nome"]} tem carteira de trabalho? (0 para não): '))
print('-=' * 30)
if dados['carteira'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - ano_atual
for k,v in dados.items():
    print(f' - {k} tem o valor {v}')

boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('~' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, v in enumerate(boletim):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8}')
aluno = 0
while aluno != 999:
    aluno = int(input('Mostrar notas de qual aluno? (999 para parar): '))
    for i, v in enumerate(boletim):
        if i == aluno:
            print(f'Notas de {v[0]} são {v[1]}')
    print('-' * 30)
print('Finalizado!')

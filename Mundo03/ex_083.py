expressao = str(input('Digite uma expressão: '))
cont_aberto = cont_fechado = 0
for simb in expressao:
    if simb == '(':
        cont_aberto += 1
    elif simb == ')':
        cont_fechado += 1
if cont_aberto == cont_fechado:
    print('Expressão correta!')
elif cont_aberto != cont_fechado:
    print('Expressão incorreta!')
        
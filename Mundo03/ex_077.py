lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis','estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for i in lista:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

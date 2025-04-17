numeros = ('Zero', 'um', 'Dois','Três', 'Quatro',
           'cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 
           'Quinze','Dezeseis', 'Dezoito', 'Dezenove', 'Vinte' )
while True:
    num = int(input('Insira um número de 0 a 20: '))
    if num >= 0 and num <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'O numero {num} em extenso fica: {numeros[num]}')

def area(larg,com):
    a = larg * com
    print(f'A área de um  terreno {larg} X {com} é {a} m²')

print(' Controle de terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)
  
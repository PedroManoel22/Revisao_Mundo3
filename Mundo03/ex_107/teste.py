from moedas import dobro, metade, aumentar, diminuir
p = float(input('Digite um preço: '))
print(f'O dobro de R${p} é R${dobro(p):.1f}')
print(f'A metade de R${p} é R${metade(p):.1f}')
print(f'Aumentando 10% de {p} fica {aumentar(p,10)}')
print(f'Diminuindo 10% de {p} fica {diminuir(p,10)}')

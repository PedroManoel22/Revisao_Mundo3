from moeda import dobro, metade, aumentar, diminuir, formatação
p = float(input('Digite um preço: '))
print(f'O dobro de R${formatação(p)} é R${formatação(dobro(p))}')
print(f'A metade de R${formatação(p)} é R${formatação(metade(p))}')
print(f'Aumentando 10% de {formatação(p)} fica {formatação(aumentar(p,10))}')
print(f'Diminuindo 10% de {formatação(p)} fica {formatação(diminuir(p,10))}')

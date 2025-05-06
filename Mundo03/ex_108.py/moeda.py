def dobro(preço):
    return preço * 2


def metade(preço):
    return preço / 2


def aumentar(preço,taxa):
    return preço + (preço * taxa/100)


def diminuir(preço,taxa):
    return preço - (preço * taxa/100)


def formatação(preço, moeda= 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

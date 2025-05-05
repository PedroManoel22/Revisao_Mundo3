def notas(*x, sit=False):
    soma = 0
    r = dict()
    r['total'] = len(x)
    for i in range(0, len(x)):
        soma += x[i]
        if i == 0:
            r['menor'] = r['maior'] = x[i]
        else:
            if x[i] > r['maior']:
                r['maior'] = x[i]
            if x[i] < r['menor']:
                r['menor'] = x[i]
    r['média'] = soma / len(x)
    if sit:
        if r['média'] < 7 and r['média'] >= 5:
            r['situação'] = 'Em recuperação'
        elif r['média'] >= 7:
            r['situação'] = 'Aprovado'
        else:
            r['situação'] = 'Reprovado'  
    return r
resp = notas(5.5, 2.5, 0, sit=True)
print(resp)

from time import sleep
def contagem(i,f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')  
contagem(1,10,1)
contagem(10,0,2)
print('Agora é a sua vez de personalizar a contagem!')
x = int(input('Inicio: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
contagem(x,y,z)

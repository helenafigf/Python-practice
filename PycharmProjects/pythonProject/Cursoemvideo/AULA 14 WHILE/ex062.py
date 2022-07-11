pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = pt
cont = 0
while cont < 10:
    print(termo,end=' -> ')
    cont+= 1
    termo += razao
m = int(input('\nQuantos termos você quer mostrar a mais? '))
if m != 0:
    while cont == 20:
        termo += razao
        print(termo, end=' ')
        cont += 1
else:
    print('Fim')
    print(f'Progressão finalizada com {cont} termos mostrados.')



pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = pt
cont = 0
while cont < 10:
    print(termo,end=' -> ')
    cont+= 1
    termo += razao
print('FIM')
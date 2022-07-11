print(50*'=')
print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print(50*'=')
cont = 0
pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = pt + (10*razao)
for c in range (pt,cont,razao):
    print(c,end=' -> ')
print('fim')
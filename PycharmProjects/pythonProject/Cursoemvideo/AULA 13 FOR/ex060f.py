n = int(input('Digite um número: '))
f = 1
print(f'Calculando {n}! = ',end='')
for c in range (n,0,-1):
    print(f'{c} x ',end='')
    f*=c
print(f' = {f}',end='')


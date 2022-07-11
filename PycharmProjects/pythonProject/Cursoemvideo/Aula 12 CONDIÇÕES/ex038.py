n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

print(100*'=')
print('\033[7m''COMPARANDO VALORES...')


if n1 < n2:
    print(f'{n1} é menor que {n2}')
elif n1 > n2:
    print(f'{n1} é maior que {n2}')
else:
    print('Os dois valores são iguais')

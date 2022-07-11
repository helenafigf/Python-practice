'''
maior = 0
menor = 0
for c in range (1,6):
    peso = float(input(f'Digite o peso da {c}° pessoa:'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}kg')
print(f'O menor peso lido foi {menor}kg')
'''
lista = []
for c in range (1,6):
    pesos = float(input(f'Digite o peso da {c}º pessoa: '))
    lista += [pesos]
print(f'O maior peso é {max(lista)}kg')
print(f'O menor peso é {min(lista)}kg')

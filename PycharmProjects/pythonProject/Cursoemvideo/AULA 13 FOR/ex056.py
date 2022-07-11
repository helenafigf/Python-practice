'''
imenor = 0
imaior = 0
lista = []
for c in range (1,5):
    print(f'{c}°PESSOA')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: '))
    lista += [idade]
print(f'O homem mais velho é o {max.[idade]}')
'''
imenor = 0
imaior = 0
count_age= 0
xm = 0
for c in range (1,5):
    print(f'{c}°PESSOA')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: '))
    count_age += idade
    if sexo == 'F' and idade <= 20:
        xm+= 1
    else:
        if idade ==1:
            imenor = idade
            imaior: idade
        else:
            if idade > imaior and sexo == 'M':
                imaior = idade
                hnome = nome
            else:
                imenor = idade

media = count_age/4
print(f'A média de idade do grupo é {media}')
print(f'O homem mais velho tem {imaior} e se chama {hnome}')
print(f'Temos {xm} mulheres com menos de 20 anos de idade')
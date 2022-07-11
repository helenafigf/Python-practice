import math

casa = float(input('Insira o valor da casa:R$'))
salário = float(input('Insira sua renda mensal:R$'))
ano = int(input('Em quantos anos deseja pagar?'))

a = ano*12
vprest = casa/a
pct = salário*30/100

if vprest >= pct:
    print('\033[4:30:41m'f'Infelizmente você não poderá pegar este empréstimo')
else:
    print('\033[4:30:42m'f'Você está autorizado a solicitar esse empréstimo')
print(f'O valor da prestação será de R${vprest:.2f}')
print(f'30% do seu salário corresponde a R${pct}')
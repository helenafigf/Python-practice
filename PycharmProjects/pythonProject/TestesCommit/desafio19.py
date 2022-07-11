import random
a = input('Digite o nome de seu aluno: ')
b = input ('Digite o nome de seu aluno: ')
c = input('Digite o nome de seu aluno: ')
d = input('Digite o nome de seu aluno: ')
lista = [a,b,c,d]
print('\033[7:30:44m' f'O aluno escolhido foi:{random.choices(lista)}')
from random import randint
computador = randint(0,5)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
jogador = int(input("Em que número eu pensei?"))
if jogador == computador:
     print('PARABENS!')
else:
     print(f'Ganhei, eu pensei no número {computador} e não no {jogador}')
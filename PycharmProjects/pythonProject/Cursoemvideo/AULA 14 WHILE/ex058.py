import random
print ('Sou seu computador...')
print('Tente adivinhar o número que estou pensando')
print('Está entre 0 e 10')
n1 = random.randint(0,10)
c = 0
jogador = int(input('Digite um valor de 1 a 10: '))
#print(n1)
c +1

while n1 != jogador:

    if jogador > n1:
        jogador = int(input('Menos...Tente mais uma vez!'))
        c += 1
    elif jogador < n1:
        jogador = int(input('Mais..Tente mais uma vez.'))
        c +=1
print(f'Fim do jogo, você acertou em {c} tentativas.')

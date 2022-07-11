from random import choice
hand = str(input('pedra, papel ou tesoura: '))
seq = ['pedra','papel','tesoura']
computer = (choice(seq))


if hand == 'pedra' and computer == 'papel':
    print ('\033[0:30:47m'f'{hand} X {computer}: PAPEL COBRE PEDRA, VOCÊ PERDEU')
elif hand == 'pedra' and computer == 'pedra':
    print ('\033[0:30:47m'f'{hand} X {computer}: EMPATE')
elif hand == 'pedra' and computer == 'tesoura':
    print('\033[0:30:47m'f'{hand} X {computer}: PEDRA QUEBRA TESOURA, PARABÉNS')

elif hand == 'tesoura' and computer == 'papel':
    print ('\033[0:30:47m'f'{hand} X {computer}: TESOURA CORTA PAPEL, PARABÉNS')
elif hand == 'tesoura' and computer == 'tesoura':
    print('\033[0:30:47m'f'{hand} X {computer}: EMPATE')
elif hand == 'tesoura' and computer == 'pedra':
    print ('\033[0:30:47m'f'{hand} X {computer}: PEDRA QUEBRA TESOURA, VOCÊ PERDEU')

if hand == 'papel' and computer == 'papel':
    print('\033[0:30:47m'f'{hand} X {computer}: EMPATE')
elif hand == 'papel' and computer == 'tesoura':
    print('\033[0:30:47m'f'{hand} X {computer}: TESOURA CORTA PAPEL, VOCê PERDEU')
elif hand == 'papel' and computer == 'pedra':
    print('\033[0:30:47m'f'{hand} X {computer}: PAPEL COBRE PEDRA, PARABÉNS!')
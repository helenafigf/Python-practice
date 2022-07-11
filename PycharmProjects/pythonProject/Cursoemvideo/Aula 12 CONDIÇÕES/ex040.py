
nota1= float(input('Digite sua nota: '))
nota2= float(input('Digite sua nota: '))

R = (nota1+nota2)/2
print(f'Sua média é {R:.1f}, portanto você está:')
if R < 5:
    print('\033[0:30:41m''REPROVADO')
elif R >= 7:
    print('\033[0:30:42m''Aprovado')
elif R >=5 or R <=6.9:
    print('\033[0:30:43m''RECUPERAÇÃO')


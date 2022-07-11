p = float(input('Digite o preço do produto: '))
f = str(input('Digite a forma de pagamento: '))

print('Calculando seu desconto . . . ')

din = p * 10/100
dd = p - din
car = p *5/100
ddc = p - car
juros = p * 20/100
tj = p + juros


if f == 'dinheiro':
    print('\033[0:30:42m'f'Você tem desconto de 10%, valor final será R${dd}')
elif f == '1x no cartão':
    print('\033[0:30:42m'f'Você tem desconto de 5%, valor final será R${ddc}')
elif f == '2x no cartão':
    print('\033[0:30:43m'f'Você não tem descontos')
elif f == '3x no cartão':
    print('\033[0:30:41m'f'Você tem juros de 20%, valor final será R${tj}')
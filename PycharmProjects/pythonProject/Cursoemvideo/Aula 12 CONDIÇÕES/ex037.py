#conversor de bases
num = int(input('Digite um número qualquer: '))
c = int(input('[1]Converter em base binária \n'
              '[2]Converter em base octal\n'
              '[3]Converter em base hexadecimal'))
#c1 = bin(int,num)
#c2 = oct(int,num)
#c3 = hex(int,num)
if c == 1:
    print(f'{num} convertido para base binária {bin(num)[2:]}')
elif c == 2:
    print (f'{num} convertido para base octal {oct(num)[2:]}')
elif c == 3:
    print(f'{num} convertido para base hexadecimal {hex(num)[2:]}')
else:
    print('Opção inválida')
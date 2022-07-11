num = int(input('Digite um número: '))
cont = 0
for c in range (1,num+1):
            #print(c, end = ' ')
            #div = num % c
        if num % c == 0 and num % num == 0:
            print( f'\033[1;92m {c}', end=' ')
            cont += 1
        else:
            print( f'\033[1;91m {c}',end=' ')
print(f'\n O número {num} foi divisível {cont} vezes')
if cont == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele NÃO é primo')





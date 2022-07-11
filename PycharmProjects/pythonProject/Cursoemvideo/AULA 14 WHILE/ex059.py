from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
somar = n1+n2
mult = n1*n2
opcao = int(input('''O que você quer fazer?
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Outros valores
    [5]Sair do programa'''))

while opcao != 5:
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {somar}')
        opcao = int(input('''O que você quer fazer?
            [1]Somar
            [2]Multiplicar
            [3]Maior
            [4]Outros valores
            [5]Sair do programa'''))
    elif opcao == 2:
        print(f'A multiplicação de {n1} e {n2} corresponde a {mult}')
        opcao = int(input('''O que você quer fazer?
            [1]Somar
            [2]Multiplicar
            [3]Maior
            [4]Outros valores
            [5]Sair do programa'''))
    elif opcao ==3:
        if n1 == n2:
            print(f'Os valores digitado são iguais')
            opcao = int(input('''O que você quer fazer?
                [1]Somar
                [2]Multiplicar
                [3]Maior
                [4]Outros valores
                [5]Sair do programa'''))
        elif n1 > n2:
            print(f'{n1} é maior que {n2}')
            opcao = int(input('''O que você quer fazer?
                [1]Somar
                [2]Multiplicar
                [3]Maior
                [4]Outros valores
                [5]Sair do programa'''))
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
            opcao = int(input('''O que você quer fazer?
                [1]Somar
                [2]Multiplicar
                [3]Maior
                [4]Outros valores
                [5]Sair do programa'''))
    elif opcao == 4:
        print('Insira novos valores abaixo')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        somar = n1 + n2
        mult = n1 * n2
        opcao = int(input('''O que você quer fazer?
            [1]Somar
            [2]Multiplicar
            [3]Maior
            [4]Outros valores
            [5]Sair do programa'''))
    else:
        print('Opção inválida')
        opcao = int(input('''O que você quer fazer?
            [1]Somar
            [2]Multiplicar
            [3]Maior
            [4]Outros valores
            [5]Sair do programa'''))
    sleep(2)
print('Fim do programa')
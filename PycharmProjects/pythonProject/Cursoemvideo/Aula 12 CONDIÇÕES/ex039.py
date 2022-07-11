import datetime
current_time = datetime.datetime.now()
ano = current_time.year

sexo = int(input('Tecle 1 se você for homem e 2 se for mulher: '))
if sexo == 1 :
    nasc = int(input('Em que ano você nasceu: '))
    x = ano - nasc
    falta = 18 - x
    atraso = x - 18
    if x == 18:
            print(f'Você tem {x}')
            print('É ano de alistamento')
    elif x < 18:
            print(f'Você tem {x}')
            print('Ainda não é a sua vez de se alistar')
            print(f'Faltam {falta} ano(s) para a sua vez')
    elif x > 18:
            print(f'Você tem {x}')
            print('Espero que você já tenha se alistado')
            print(f'Você está {atraso} ano(s) atrasado')
else:
    print('Mulheres não são obrigadas a se alistar')
#from date time import date
#ano = date.today().year

import datetime
current_time = datetime.datetime.now()
ano = current_time.year
cont1 = 0
cont2 = 0

for c in range (1,8):
    id = int(input(f'Digite o ano em que a {c}° pessoa nasceu: '))
    if ano - id >= 18:
            cont1 += 1
    else:
            cont2 += 1
print(f'Temos {cont1} pessoas maiores de idade.'
       f'\n E {cont2} menores de idade')

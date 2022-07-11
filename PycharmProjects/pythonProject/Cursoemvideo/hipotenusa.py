import math
c1 = float(input('Digite o valor do cateto op: '))
c2 = float(input('Digite o valor do cateto adj: '))

hip = math.hypot(c1,c2)

print(f'O valor da hipotenusa corresponde a {hip:.2f} ')
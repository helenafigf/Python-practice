
from math import factorial
n = int(input('Digite um número: '))
for c in range (n,0,-1):
    print(c,'x',end='')
r=(factorial(n))
print(f' {n}! = {r}',end='')


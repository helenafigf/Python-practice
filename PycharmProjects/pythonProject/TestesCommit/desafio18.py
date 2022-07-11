import math
ang = float(input('Digite um ângulo: '))

s = math.sin(math.radians(ang))
t = math.tan(math.radians(ang))
c = math.cos(math.radians(ang))

print(f'O seno de {ang} é {s:.2}\nA tangente de {ang} é {t:.2}\nO cosseno de {ang} é {c:.2}.')
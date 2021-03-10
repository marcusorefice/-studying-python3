import math
a: float = int(input('Digite um angulo: '))
seno = math.sin(math.radians(a))
coss = math.cos(math.radians(a))
tang = math.tan(math.radians(a))
print(f'O seno de {a} é {(seno):.2f} o cosseno é {(coss):.2f} e a tangente é {(tang):.2f}')
'''Refaca o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes'''

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Pode formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO pois tem todos os lados iguais.')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('O triângulo é ISÓSCELES pois tem dois lados iguais')
    else:
        print('O triângulo é ESCALENO pois tem todos os lados diferentes')
else:
    print('Não se pode formar um triângulo')


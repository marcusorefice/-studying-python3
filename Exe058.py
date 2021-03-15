'''Melhore o jogo DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.'''

from random import randint
cont = 0
n = 0
r = randint(0, 10)
acertou = False
while not acertou:
    n = int(input('Adivinhe o número entre 0 a 10: '))
    cont += 1
    if n == r:
        acertou = True
    else:
        if n < r:
            print(f'É maior que {n} tente de novo.')
        elif n > r:
            print(f'É menor que {n}, tente de novo.')
print(f'VOCÊ ACERTOU com {cont} tentativas.')

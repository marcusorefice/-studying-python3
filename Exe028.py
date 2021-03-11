'''Desafio 028
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela do usuário venceu ou perdeu.'''

from random import randint
n = int(input('Adivinhe o número de 0 a 5: '))
r = int(randint(0, 5))
if r == n:
    print('Você venceu!')
else:
    print(f'Você perdeu, o número era {r}')

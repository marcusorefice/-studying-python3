"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ordem = {}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ordem = sorted(jogo.items(), key=itemgetter(1), reverse=(True))
print('-=-'*20)
print('  == RANKING DOS JOGADORES ==')
for k, v in enumerate(ordem):
    print(f'   {k+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.8)

"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e maior valor que estão na tupla."""

from random import randint
n1 = (randint(1, 10), randint(1, 10), randint(1, 10),
      randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for c in n1:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi o {max(n1)}')
print(f'O menor valor sorteado foi o {min(n1)}')

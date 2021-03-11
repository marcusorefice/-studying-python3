'''Crie um programa que faça o computador jogar Jokenpê com você.'''

from random import randint
j = int(input('Você quer: \n[1] PEDRA \U0000270A \n[2] PAPEL \U0000270B \n[3] TESOURA \U0000270C \n'))
print('-'*30)
r = int(randint(1, 3))
if j == 1 and r == 3:
    print(f'VOCÊ GANHOU! O computador colocou TESOURA\U0000270C')
elif j == 2 and r == 1:
    print(f'VOCÊ GANHOU! O computador colocou PEDRA\U0000270A')
elif j == 3 and r == 2:
    print(f'VOCÊ GANHOU! O computador colocou PAPEL\U0000270B')
elif j == 1 and r == 1 or j == 2 and r == 2 or j == 3 and r == 3:
    print(f'EMPATOU')
elif j == 1 and r == 2:
    print(f'O COMPUTADOR GANHOU! Colocou PAPEL\U0000270B')
elif j == 2 and r == 3:
    print(f'O COMPUTADOR GANHOU! Colocou TESOURA \U0000270C')
elif j == 3 and r == 1:
    print('O COMPUTADOR GANHOU! Colocou PEDRA \U0000270A')
else:
    print('OPÇÃO INVÁLIDA')
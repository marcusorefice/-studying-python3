'''Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
No final, mostre os 10 primeiros termos dessa progressão.'''
print('-'*30)
print('10 TERMOS DE UMA PA')
print('-'*30)
ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
dec = ter + (10 - 1) * raz
for c in range(ter, dec + raz, raz):
    print(f'{c}',end=' → ')
print('ACABOU')
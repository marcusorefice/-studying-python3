'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.'''

from _datetime import date

dataa = date.today().year
s1 = 0
s2 = 0
for c in range(1, 8):
    data = int(input(f'Digite o {c}º ano de nascimento: '))
    if dataa - data >= 21:
        s1 += 1
    else:
        s2 += 1
print(f'{s1} pessoas já atingiram a maioridade \n{s2} pessoas ainda não atingiram a maioridade.')

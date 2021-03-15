'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.'''

print('=-'*15)
print('            LOJÃO')
print('-='*15)
cont = 0
somapreco = 0
menor = 0
cont1 = 0
nomemenor = ''
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: R$'))
    cont1 += 1
    print('-'*30)
    somapreco += preco
    if preco >= 1000:
        cont += 1
    if cont1 == 1 or preco < menor:
        menor = preco
        nomemenor = nome
    con = input('Deseja continuar? [S/N]').upper()
    if con == 'N':
        print(f'O total gasto na compra foi de {somapreco:.2f}')
        print(f'O total de produtos que custam mais de R$1000 é {cont}')
        print(f'O produto mais barato é {nomemenor}')
        break

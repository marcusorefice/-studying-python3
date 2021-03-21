"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves."""

lista = []
temp = []
maior = menor = 0
while True:
    temp.append(input('Digite um nome: '))
    temp.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    s = input('Quer continuar? [S/N] ').upper()
    if s in 'N':
        break
print('-'*40)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {maior:.2f}kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor:.2f}kg. Peso de ',end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')

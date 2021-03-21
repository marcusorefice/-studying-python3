"""Faça um programa que leia 5 valores numéricos e guarde os em uma lista.
No final, mostre qual foi o maior valor e o menor valor digitado e as suas respectivas posições na lista."""

lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a {c}ª posição: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('-'*40)
print(f'Os números digitados são: {lista}')
print(f'O maior valor é {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}, ', end='')
print(f'\nO menor valor é {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}, ', end='')
print()

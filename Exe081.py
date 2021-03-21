"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A)Quantos números foram digitados.
B)A lista de valores ordenada de forma decrescente.
C)Se o valor 5 foi digitado e está ou não na lista."""

lista = []
while True:
    lista.append(int(input(f'Digite um valor: ')))
    s = input('Quer continuar? [S/N] ').upper()
    if s in 'N':
        break
print('-' * 50)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista na ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')

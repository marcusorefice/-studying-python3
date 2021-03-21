"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas lista extras que vão conter apenas os valores pares e os valores impares
digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    s = input('Quer continuar? [S/N] ').upper()
    if s == 'N':
        break
print('-'*40)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listap}')
print(f'A lista de ímpares é {listai}')

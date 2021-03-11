'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''

n = float(input('Digite o 1º número: '))
n1 = float(input('Digite o 2º número: '))
n2 = float(input('Digite o 3º número: '))
menor = n
maior = n
if n1 < menor:
    menor = n1
if n2 < menor:
    menor = n2
print(f'O menor número é: {menor:.2f}')
if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
print(f'O maior número é: {maior:.2f}')
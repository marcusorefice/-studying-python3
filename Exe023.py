'''Desafio 023
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex.:
Digite um número: 1834

Unidade: 4  Dezena: 3 Centena: 8  Milhar: 1'''


n = (input('Digite um número de 0 a 9999: '))
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')

'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais o aumento é 15%.'''

s = float(input('Qual é o salário a ser calculado? '))
a = (s*10)/100
b = (s*15)/100
if s >= 1250:
    print(f'O novo salário com 10% de aumento é: {s+a}')
else:
    print(f'O novo salário com 15% de aumento é: {s+b}')

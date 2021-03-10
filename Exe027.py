'''Desafio 027
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex.: Ana Maria de Souza
Primeiro = Ana
Último = Souza'''

n = input('Digite seu nome completo: ').strip()
m = n.split()
print(f'O primeiro nome é: {m[0]} \nO ultimo nome é: {m[-1]}')

'''Desafio 025
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

c = input('Digite um nome: ').upper().strip()
print(f'O nome tem Silva?: {"SILVA" in c}')

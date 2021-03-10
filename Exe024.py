'''Desafio 024
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"'''


c = input('Digite o nome de uma cidade: ').upper().strip()
print(f'Começa com Santo: {"SANTO" in c[:5]}')
#ou print(c[:5] == 'Santo')

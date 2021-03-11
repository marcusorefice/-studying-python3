'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR'''

n = int(input('Digite um número inteiro: '))
r = (n % 2 == 0)
if r == True:
    print(f'O valor é PAR')
else:
    print(f'O valor é IMPAR')
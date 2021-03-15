'''Crie um programa que leia a idade o sexo de várias pesosas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''

contidade = 0
contsexoM = 0
contfi = 0
sexo = ' '
print('-'*30, '\n     CADASTRE UMA PESSOA')
print('-'*30)
while True:
    idade = input('Digite a idade: ')
    sexo = input('Digite o sexo: [M/F] ').strip().upper()
    print('-' * 30)
    cont = input('Quer continuar? [S/N] ').upper()
    if idade >= '18':
        contidade += 1
    if sexo == 'M':
        contsexoM += 1
    if idade < '20' and sexo == 'F':
        contfi += 1
    if cont == 'N':
        print(f'{contidade} pessoas tem mais de 18 anos. \n{contsexoM} homens cadastrados. \n{contfi} mulheres tem menos'
              ' de 20 anos.')
        break

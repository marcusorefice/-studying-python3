""" Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""

aluno = {}
lista = []
aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
lista.append(aluno.copy())
print('-'*40)
print(f'-Nome é igual a {aluno["nome"]}')
print(f'-Média é igual a {aluno["media"]}')
if aluno['media'] >= 7:
    print('-Situação é igual APROVADO!')
elif 5 <= aluno['media'] < 7:
    print('-Situação é igual RECUPERAÇÃO')
else:
    print('-Situação é igual REPROVADO!')

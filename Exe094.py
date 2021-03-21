"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

# dados['nome'] = input('Nome: ')
# dados['idade'] = data - int(input('Ano de nascimento: '))
# dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

pessoas = {}
lista = []
soma = 0
while True:
    pessoas['nome'] = input('Nome: ')
    while True:
        pessoas['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {soma/len(lista):.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= soma/len(lista):
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()

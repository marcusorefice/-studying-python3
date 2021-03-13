'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos.'''


midade = 0
conidade = 0
connome = ''
consexo = ''
tot20 = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = input('NOME: ').strip()
    idade = int(input('IDADE: '))
    sexo = input('SEXO (M/F): ').strip()
    midade += idade
    if c == 1 and sexo in 'Mm':
        conidade = idade
        connome = nome
    if sexo in 'Mm' and idade > conidade:
        conidade = idade
        connome = nome
    if sexo in 'Ff' and idade < 20:
        tot20 += 1

print(f'A média de idade do grupo é: {midade / 4:.2f}')
print(f'O homem mais velho tem {conidade} anos e se chama {connome}.')
print(f'Ao todo são {tot20} mulheres com menos de 20 anos.')

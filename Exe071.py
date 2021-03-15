'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=-'*20)
print('            CAIXA ELETRÔNICO')
print('-='*20)
print('O caixa possui cédulas de: \nR$50,00 \nR$20,00 \nR$10,00 \nR$1,00')
print('-'*40)
valor = int(input('Digite o valor a ser sacado: R$'))
resto50 = valor // 50
resto50r = resto50 * 50
aux50 = valor - resto50r
resto20 = aux50 // 20
resto20r = resto20 * 20
aux20 = aux50 - resto20r
resto10 = aux20 // 10
resto10r = resto10 * 10
resto1 = aux20 - resto10r
if resto50 > 0:
    print(f'Total de {resto50} cédulas de R$50')
if resto20 > 0:
    print(f'Total de {resto20} cédulas de R$20')
if resto10 > 0:
    print(f'Total de {resto10} cédulas de R$10')
if resto1 > 0:
    print(f'Total de {resto1} cédulas de R$1')
print('='*40)
print('VOLTE SEMPRE!')

'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os primeiros termos
da progressão usando a estrutura while.'''

print('-'*30)
print('10 TERMOS DE UMA PA')
print('-'*30)
ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
cont = 10
while cont != 0:
    print(ter, end=' → ')
    ter += raz
    cont -= 1
print('ACABOU')

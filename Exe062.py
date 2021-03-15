'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.'''

print('-'*30)
print('10 TERMOS DE UMA PA')
print('-'*30)
primeiro = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
ter = primeiro
cont = 1
mais = 10
tot = 0
while mais != 0:
    tot += mais
    while cont <= tot:
        print(f'{ter}', end=' → ')
        ter += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Foram mostrados {tot} termos')

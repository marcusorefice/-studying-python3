'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

cond = ''
media = 0
maior = 0
menor = 0
soma = 0
while cond != 'N':
    n = int(input('Digite um número: '))
    cond = input('Deseja continuar? (S/N)').upper()
    media += 1
    soma += n
    if media == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'A média dos números foi {soma/media:1} \nO maior número foi {maior} \nO menor número foi {menor}')

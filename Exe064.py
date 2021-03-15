'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de para. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (descosiderando o flag).'''

n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número ou 999 para fechar o programa: '))
    if n != 999:
        soma += n
        cont += 1
print(f'Foram digitados {cont} e a soma deles foi de: {soma}')

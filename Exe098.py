"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada
A) de 1 até 10, de 1 em 1
B) de 10 até 0, de 2 em 2
C) uma contagem personalizada"""

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(3)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('agora é sua vez de personalizar a contagem!')
i = (int(input('Digite o inicio ')))
f = (int(input('Digite o fim ')))
p = int(input('Digite o passo '))
contador(i, f, p)

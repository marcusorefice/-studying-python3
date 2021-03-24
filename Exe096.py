"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""


def area(larg, comp):
    ar = larg * comp
    print(f'A área de um terreno de {larg:.2f}x{comp:.2f} é de {ar:.2f}m².')


print('Cálculo de área')
print('-' * 20)
l = (float(input('LARGURA (m): ')))
c = (float(input('COMPRIMENTO (m): ')))
area(l, c)

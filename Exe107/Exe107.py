"""Crie um módulo chamado Exe107moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções."""

import Exe107moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${Exe107moeda.metade(p)}')
print(f'O dobro de R${p} é R${Exe107moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${Exe107moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos R${Exe107moeda.diminuir(p, 13)}')

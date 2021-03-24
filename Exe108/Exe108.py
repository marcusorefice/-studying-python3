"""Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar
os números como um valor monetário formatado."""

import Exe108moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {Exe108moeda.moeda(p)} é {Exe108moeda.moeda(Exe108moeda.metade(p))}')
print(f'O dobro de {Exe108moeda.moeda(p)} é {Exe108moeda.moeda(Exe108moeda.dobro(p))}')
print(f'Aumentando 10%, temos {Exe108moeda.moeda(Exe108moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {Exe108moeda.moeda(Exe108moeda.diminuir(p, 13))}')

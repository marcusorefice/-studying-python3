'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''

from datetime import date
ano = int(input('Digite o ano de nascimento: '))
a = date.today().year
if a - ano < 18:
    print(f'O jovem tem {a-ano} anos e ainda vai se alistar ao serviço militar \nFaltam {18-(a-ano)} anos para se alistar!')
elif a - ano == 18:
    print(f'O jovem tem {a-ano} anos e está na hora de se alistar ao serviço militar')
else:
    print(f'Já tem {a-ano} anos e passou {(a-ano)-18} anos do tempo de alistamento')

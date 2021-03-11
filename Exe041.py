'''A confederação Naciona de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre mostre sua categoria, de acordo com a idade:
Até 9 anos:MIRIM
Até 14 anos:INFANTIL
Até 19 anos:Junior
Até 25 anos:Sênior
Acima:MASTER'''

from datetime import date
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'O atleta tem {idade} anos e é da categoria MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e é da categoria INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos e é da categoria JUNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e é da categoria SÊNIOR')
else:
    print(f'O atleta tem acima de {idade} anos e é da categoria MASTER')

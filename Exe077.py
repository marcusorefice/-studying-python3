"""Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')

for cont in palavras:
    print(f'\nNa palavra {cont} temos ', end='')
    for letra in cont.lower():
        if letra in 'aeiou':
            print(letra, end=' ')

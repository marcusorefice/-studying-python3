"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A)Quantas vezes apareceu o valor 9.
B)Em que posição foi digitado o primeiro valor 3.
C)Quais foram os números pares."""

v1 = (int(input('Digite o primeiro valor: ')),
      int(input('Digite o segundo valor: ')),
      int(input('Digite o terceiro valor: ')),
      int(input('Digite o quarto valor: ')))
print(f'Você digitou os números: {v1}')
print(f'O número 9 foi digitado {v1.count(9)} vezes')
if 3 in v1:
    print(f'O primeiro 3 foi digitado na posição {v1.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in v1:
    if n % 2 == 0:
        print(n, end=' ')

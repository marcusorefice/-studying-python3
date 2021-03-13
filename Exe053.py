'''Crie um programa que leia uma frase e diga se ela é palíndromo, desconsiderando os espaços.
Ex: APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA'''

frase = input('Digite uma frase: ').upper()
frase = frase.replace(' ', '')
pali = frase[::-1]
print(f'O inverso de {frase} é {pali}')
if pali == frase:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
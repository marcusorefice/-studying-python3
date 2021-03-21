'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostra-lo por extenso.'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {numeros[n]}')
    else:
        print('Tente novamente.')
    if 0 <= n <= 20:
        s = input('Quer continuar? [S/N] ').upper()
        if s != 'S':
            break

'''Faça um programa que calcule a soma de todos os números impares que são multiplos de três
e que se encontram no intervalo de 1 até 500'''

r = 0
cont = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
            cont += + 1
            r += + c
print(f'A soma de todos os {cont} valores impares e multiplos de 3 no intervalo de 1 até 500 é: {r}')

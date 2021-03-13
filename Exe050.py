'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o'''

s = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        s += num
        cont += +1
print(f'Você informou {cont} números pares e a soma é: {s}')

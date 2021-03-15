'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma sequência de Fibonacci.'''

n = int(input('Digite quantos números de Fibonacci você quer ver: '))
f1 = 0
f2 = 1
s = 0
cont = 3
print(f'{f1} → {f2}',end='')
while cont <= n:
    s = f1 + f2
    print(f' → {s}', end='')
    f1 = f2
    f2 = s
    cont += 1
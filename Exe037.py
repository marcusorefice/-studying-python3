'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão:
1 para binário
2 para octal
3 para hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif op == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif op == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('OPÇÃO INVÁLIDA')

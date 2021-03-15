'''Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

s = 0
op = 4
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
while op != 5:
        print('-'*15, 'MENU', '-'*15)
        print('[1]SOMAR')
        print('[2]MULTIPLICAR')
        print('[3]MAIOR')
        print('[4]NOVOS NÚMEROS')
        print('[5] SAIR DO PROGRAMA')
        op = int(input('ESCOLHA UMA OPÇÃO DO MENU: '))
        print('-' * 15, 'MENU', '-' * 15)
        if op == 1:
            s = n1 + n2
            print(f'A soma dos números é: {s:.2f}')
        elif op == 2:
            s = n1 * n2
            print(f'A multiplicação dos números é: {s:.2f}')
        elif op == 3:
            if n1 > n2:
                print(f'{n1:.2f} é o maior número!')
            else:
                print(f'{n2:.2f} é o maior número!')
        elif op == 4:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
        elif op == 5:
             print('Saindo...')
        else:
            print('Opção inválida, tente novamente!')
print('Volte sempre!')

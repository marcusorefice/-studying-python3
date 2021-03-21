"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso
o número já exista lá dentro, ele não sera adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar.!')
    s = input('Deseja continuar? [S/N]').upper()
    if s != 'S':
        lista.sort()
        print('-'*70)
        print(f'Os valores digitados em ordem crescente são {lista}')
        break

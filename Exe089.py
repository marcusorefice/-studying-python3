"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente."""

lista = []
bol = []
while True:
    aluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append(aluno)
    lista.append(nota1)
    lista.append(nota2)
    bol.append(lista[:])
    lista.clear()
    s = input('Deseja continuar? [S/N] ').upper()
    if s != 'S':
        print('-'*30)
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>15}')
for i, l in enumerate(bol):
    print(f'{i:<4}{l[0]:<10}{(l[1]+l[2])/2:>15}')
print('-'*30)
while True:
    n = int(input('Deseja ver as notas de qual aluno? (999 fecha o programa): '))
    print(f'As nota de {bol[n][0]} são [{bol[n][1]}, {bol[n][2]}]')
    if n == 999:
        break

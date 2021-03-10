from random import sample
a = input('Digite o nome do 1º aluno: ')
b = input('Digite o nome do 2º aluno: ')
c = input('Digite o nome do 3º aluno: ')
d = input('Digite o nome do 4º aluno: ')
alunos = (a, b, c, d)
print(f'A ordem sorteada foi: {sample(alunos, 4)}')
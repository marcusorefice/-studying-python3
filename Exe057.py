'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = 'M'
while sexo != 'M' or sexo != 'F':
    sexo = input('Digite um sexo (M/F): ').strip().upper()
    if sexo in 'MF':
        if sexo == 'M':
            print('O sexo é MASCULINO!')
        elif sexo == 'F':
            print('O sexo é FEMININO!')
    else:
        print('Sexo incorreto, digite novamete!')

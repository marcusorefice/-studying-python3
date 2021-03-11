'''Crie um programa que leia duas nota de um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida:
Média abaixo de 5.0:
REPROVADO
Média entre 5.0 e 6.9:
RECUPERAÇÃO
Média 7.0 ou superior:
APROVADO'''

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
if (n1 + n2)/2 < 5:
    print(f'A média é {(n1 + n2)/2} e ficou abaixo de 5.0: \nREPROVADO!')
elif (n1 + n2)/2 >= 5 and (n1 + n2)/2 < 7:
    print(f'A média é {(n1 + n2)/2:.1f} e ficou acima de 5.0 e abaixo de 6.9: \nRECUPERAÇÃO!')
else:
    print(f'A média é {(n1 + n2)/2:.1f} e ficou acima de 7.0 \nAPROVADO!')

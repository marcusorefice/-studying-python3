"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
-Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação (opcional)"""


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    di = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}
    if sit:
        if di['média'] >= 7:
            di['situação'] = 'BOA'
        elif di['média'] >= 5:
            di['situação'] = 'RAZOÁVEL'
        else:
            di['situação'] = 'RUIM'
    return di


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)

def metade(valor=0, formato=False):
    """
    -> Calcula a metade de um determinado preço.
    :param valor: o preço que se quer reajustar.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    r = valor / 2
    return r if formato is False else moeda(r)


def dobro(valor=0, formato=False):
    """
    -> Calcula o dobro de um determinado preço.
    :param valor: o preço que se quer reajustar.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    r = valor * 2
    return r if formato is False else moeda(r)


def aumentar(valor=0, porc=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param valor: o preço que se quer reajustar.
    :param porc: qual é a porcentagem de aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    r = (valor * porc/100) + valor
    return r if formato is False else moeda(r)


def diminuir(valor=0, porc=0, formato=False):
    """
    -> Calcula a redução de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param valor: o preço que se quer reajustar.
    :param porc: qual é a porcentagem de redução.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    r = valor - (valor * porc/100)
    return r if formato is False else moeda(r)


def moeda(valor=0, moeda='R$'):
    """
    -> Faz a formatação de um preço.
    :param valor: o preço a ser formatado.
    :param moeda: a moeda que você quer usar.
    :return: o valor formatado.
    """
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, apor=10, dpor=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{apor}% de aumento: \t{aumentar(valor, apor, True)}')
    print(f'{dpor}% de redução: \t{diminuir(valor, dpor, True)}')
    print('-' * 30)

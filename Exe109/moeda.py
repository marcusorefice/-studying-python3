def metade(valor=0, formato=False):
    r = valor / 2
    return r if formato is False else moeda(valor)


def dobro(valor=0, formato=False):
    r = valor * 2
    return r if formato is False else moeda(valor)


def aumentar(valor=0, porc=0, formato=False):
    r = (valor * porc/100) + valor
    return r if formato is False else moeda(valor)


def diminuir(valor=0, porc=0, formato=False):
    r = valor - (valor * porc/100)
    return r if formato is False else moeda(valor)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
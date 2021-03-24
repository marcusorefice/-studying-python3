def metade(valor=0):
    r = valor / 2
    return r


def dobro(valor=0):
    r = valor * 2
    return r


def aumentar(valor=0, porc=0):
    r = (valor * porc/100) + valor
    return r


def diminuir(valor=0, porc=0):
    r = valor - (valor * porc/100)
    return r


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

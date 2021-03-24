def metade(valor):
    r = valor / 2
    return r


def dobro(valor):
    r = valor * 2
    return r


def aumentar(valor, porc):
    r = (valor * porc/100) + valor
    return r


def diminuir(valor, porc):
    r = valor - (valor * porc/100)
    return r

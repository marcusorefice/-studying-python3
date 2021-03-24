"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores."""

from time import sleep

c = ('\033[m',  # 0 - sem cores
     '\033[1;107m',  # 1 - Branco.
     '\033[1;41m',  # 2 - Vermelho.
     '\033[1;42m',  # 3 - Verde.
     '\033[1;43m',  # 4 - Amarelo.
     '\033[1;104m',  # 5 - Azul.
     '\033[1;105m',  # 6 - Magenta.
     '\033[1;106m',  # 7 - Cyan.
     '\033[1;47m',  # 8 - Cinza.
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 5)
    print(c[1], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(2)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = input("Função ou Biblioteca > ")
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

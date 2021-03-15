'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''



while True:
    cont = 1
    n = int(input('Deseja ver a tabuada de qual número? '))
    if n < 0:
        print(('TABUADA ENCERRADA.'))
        break
    while cont < 11:
        print(f'{n} X {cont:1} = {n*cont}')
        cont += 1

'''Faça um programa que jogue par ou impar com o computador. O joso só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
print('-='*10, 'JOGO DO PAR OU IMPAR', '=-'*10)
cont = 0
while True:
    n1 = randint(1, 10)
    n2 = int(input('Digite um número: '))
    r = n1 + n2
    par = r % 2 == 0
    impar = r % 2 == 1
    p2 = int(input('Você quer par ou impar? \n[1] IMPAR \n[2] PAR\n '))
    print('-' * 10)
    if p2 == 1 or p2 == 2:
        if par:
            print(f'Você jogou {n2} e o computador {n1}. \nO total deu {r} que é PAR. ')
            print('-' * 10)
        elif impar:
            print(f'Você jogou {n2} e o computador {n1}. \nO total deu {r} que é IMPAR.')
            print('-'*10)
        if par and p2 == 2:
            cont += 1
            print('VOCÊ VENCEU! \nVamos jogar novamente...')
        elif impar and p2 == 1:
            cont += 1
            print('VOCÊ VENCEU! \nVamos jogar novamente...')
        else:
            print(f'VOCÊ PERDEU! \nGAME OVER! Você venceu {cont} vezes.')
            break

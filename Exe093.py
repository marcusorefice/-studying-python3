"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
um dicionário, incluindo o total de gols feitos durante o campeonato."""

lista = []
soma = 0
jogador = {'nome': input('Nome do jogador: ')}
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for g in range(0, p):
    lista.append(int(input(f'Quantos gols na partida {g}? ')))
jogador['gols'] = lista[:]
jogador['total'] = sum(lista)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {p} partidas.')
for l, c in enumerate(lista):
    print(f'    => Na partida {l}, fez {c} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

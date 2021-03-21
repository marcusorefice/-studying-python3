"""Crie uma tupla preenchida com os 20 primeiros colocados da tabela Campeonato Brasileiro de Futebol, na
ordem de colocação. Depois mostre:
A)Apenas os 5 primeiros colocados.
B)Os últimos 4 colocados da tabela.
C)Uma lista com os times em ordem alfabética.
D)Em que posição na tabela está o time do Corinthians."""

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo',
         'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians',
         'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco',
         'Goiás', 'Coritiba', 'Botafogo')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-='*15)
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {(sorted(times))}')
print('-='*15)
print(f'O Corinthians está na posição {times.index("Corinthians")+1}ª posição')

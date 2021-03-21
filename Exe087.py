"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[], [], []]
par = 0
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
for l in range(0, 3):
    soma += matriz[l][2]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-'*40)
print(f'A soma dos números pares digitados é: {par}')
print(f'A soma dos valores da terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')

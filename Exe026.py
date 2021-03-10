'''Desafio 026
Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.'''

f = input('Digite uma frase: ').upper().strip()
print(f'A letra "A" aparece {f.count("A")} vezes')
print(f'A primeira vez que o "A" aparece é na posição: {f.find("A")+1}')
print(f'A ultima posição que o "A" aparece é: {f.rfind("A")+1}')
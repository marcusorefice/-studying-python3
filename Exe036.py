'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado.'''

valorc = int(input('Digite o valor da casa: R$ '))
salar = int(input('Qual é o salário? R$ '))
anos = int(input('Quantos anos quer pagar? '))
anos = anos * 12
r = valorc/anos
s = (salar*30)/100
if r > s:
    print(f'Empréstimo NEGADO! \nO valor da parcela é de R${r:.2f} e excede os 30% do salário que é de R${s:.2f}')
else:
    print(f'O empréstimo pode ser feito pois o valor da parcela é de R${r:.2f} e não excede os 30% do salário que é de R${s:.2f}')

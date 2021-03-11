'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
À vista dinheiro/cheque: 10% de desconto
À vista no cartão: 5% de desconto
em até 2x no cartão: Preço normal
3x ou mais no cartão: 20% de juros'''

valor = float(input('Digite o valor do produto: R$'))
print('-'*50)
print('Formas de pagamento disponíveis: \n[1] À VISTA(DINHEIRO/CHEQUE)(10% de desconto) \n[2] À VISTA NO CARTÃO'
'(5% de desconto) \n[3] 2X NO CARTÃO(preço normal) \n[4] 3X OU MAIS NO CARTÃO(20% de juros)')
print('-'*50)
condi = int(input('Digite a forma de pagamento: '))
desc = (valor*10)/100
if condi == 1:
    print(f'O pagamento à vista com DINHEIRO ou CHEQUE tem 10% de desconto e fica no total de R${valor-desc:.2f}')
elif condi == 2:
    print(f'O pagamento à vista com cartão tem 5% de desconto e fica no total de R${valor-(desc/2):.2f}')
elif condi == 3:
    print(f'O pagamento em 2X no cartão fica no total de R${valor:.2f} dividido em 2 parcelas de R${valor/2:.2f}')
else:
    parc = int(input('Informe em quantas vezes você quer pagar: '))
    print(f'O pagamento fica no total de {valor+(desc*2):.2f} em {parc}X de R${(valor+(desc*2))/parc:.2f}')

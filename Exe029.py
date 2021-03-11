'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.'''

v = int(input('Digite a velocidade do carro: '))
if v > 80:
    print(f'MULTADO! Excedeu o limite permitido que é de 80Km/h \nVocê deve pagar uma no valor de R${(v-80)*7:.2f}')
else:
    print('Dentro da velocidade permitida')

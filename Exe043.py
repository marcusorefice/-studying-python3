'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e
mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida'''

peso = float(input('Digite o peso de uma pessoa: (kg) '))
altura = float(input('Digite a altura de uma pessoa: (m) '))
imc = (peso/(altura**2))
print(f'O IMC é: {imc:.1f}')
if imc < 18.5:
    print('IMC abaixo de 18.5 \nA pessoa está abaixo do peso')
elif 18.5 <= imc < 25:
    print('IMC entre 18.5 e 25 \nA pessoa está com o peso ideal')
elif 25 <= imc < 30:
    print('IMC entre 25 e 30 \nA pessoa está com sobrepeso')
elif 30 <= imc < 40:
    print('IMC entre 30 e 40 \nA pessoa está com obesidade')
else:
    print('IMC acima de 40 \nA pessoa está com obesidade mórbida')

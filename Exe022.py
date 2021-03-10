'''Desafio 022
Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas
> o nome com todas as letras minúsculas
> Quantas letras ao todo (sem considerar os espaços).
> Quantas letras tem o primeiro nome.'''

n = input('Digite o nome completo: ')
print(f'O nome com todas as letras maiúsculas: {n.upper()}')
print(f'O nome com todas as letras minúscula: {n.lower()}')
e = (n.replace(' ', ''))
print(f'Quantas letras ao todo sem os espaços: {len(e)}')
dividido = n.split()
print(f'Quantas letras tem o primeiro nome: {len(dividido[0])}')

#frase = 'Curso em vídeo Python'
#frase2 = '   Aprenda Python  '
#print(len(frase)) #conta o total de letras e espaços
#print('Curso' in frase) #Tem a string 'curso' na variavel frase? True
#print(frase.replace('Python', 'Android')) #Troca a palavra Python por Android
#print(frase.find('Android')) #ele vai mostrar -1 ou se existir na string as palavras entre aspas ele mostra a posição
#print(frase.count('o'))
#print(frase.upper()) #Deixa todas as letras maiúsculas
#print(frase.lower()) #Deixa todas as letras minúsculas
#print(frase.capitalize()) #Somente a 1 letra maiúscula e o resto minúscula
#print(frase.title()) #Deixa a 1 letra e todas as letrás após o espaço maiúsculas
#print(frase2.strip())#Retira os espaços antes e e depois da string EX: de ' a ' p/ 'a'
#print(frase2.rstrip()) #Right Strip, retira somente os espaços da string no final
#print(frase2.lstrip()) #Left strip, retira somente os espaços a esquerda da string no começo
#print(frase.split()) #Ele ira criar uma divisão a cada espaço na string (Divida a string)
#print('-'.join(frase)) #No lugar do espaço, ele colocara o '-'

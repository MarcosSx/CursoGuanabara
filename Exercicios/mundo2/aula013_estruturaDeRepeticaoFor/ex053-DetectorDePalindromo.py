# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
# espaços.
palindromo = str('').replace(' ', '').upper()
palavra = str(input('Digite uma palavra: ')).replace(' ', '').upper()
for i in range(len(palavra)-1, -1, -1):
    palindromo += palavra[i]
if palavra == palindromo:
    print('{} de tras pra frente fica {}\nEsta palavra é um palindromo'.format(palavra, palindromo))
else:
    print('{} de tras pra frente fica {}\nNão é um palindromo'.format(palavra, palindromo))


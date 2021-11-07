#  Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de
#  zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',\
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    escolha = int(input('Digite um numero de 0 a 20 para ver por extenso: '))
    if escolha < 0 or escolha > 21:
        print('Numero invalido!!!', end=' ')
    if 21 > escolha > -1:
        print(f'O numero escolhido foi {escolha} e por extenso é {numeros[escolha]}')
        break

# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
numReal = float(input('Digite um numero real: '))
print('O numero {} convertido para inteiro e arredondado para mais é {} e arredondado para menos é {}'.format(numReal,
      math.ceil(numReal), math.floor(numReal)))
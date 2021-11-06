# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.
import random
print('O computador esta pensando em um numero')
numero = random.randint(0, 5)
palpite = int(input('Qual numero o computador pensou?:\n'))
print('Acertou miseravi' if numero == palpite else'Tenta denovo ai parça!!')
print('O numero pensado é: {}'.format(numero))

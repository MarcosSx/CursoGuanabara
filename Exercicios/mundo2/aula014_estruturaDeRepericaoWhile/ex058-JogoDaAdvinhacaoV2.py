# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint
from time import sleep
bot = randint(0, 10)
tentativas = 1
print('O computador esta pensando em um numero entre 0 e 10')
print('P', end='')
sleep(0.3)
print('E', end='')
sleep(0.3)
print('N', end='')
sleep(0.3)
print('S', end='')
sleep(0.3)
print('A', end='')
sleep(0.3)
print('N', end='')
sleep(0.3)
print('D', end='')
sleep(0.3)
print('O', end='')
sleep(0.3)
print('.', end='')
sleep(0.3)
print('.', end='')
sleep(0.3)
print('.\n', end='')

palpite = int(input('Qual seu palpite?\n>'))
while palpite != bot:
    if palpite > bot:
        palpite = int(input('Menos... tente novamente\n>'))
    else:
        palpite = int(input('Mais... tente novamente\n>'))
    tentativas += 1
print('Voce precisou de {} tentativas pra acertar. PARABENS!!!'.format(tentativas))

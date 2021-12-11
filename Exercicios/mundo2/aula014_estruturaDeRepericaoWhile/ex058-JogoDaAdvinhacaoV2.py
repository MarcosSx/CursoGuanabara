# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint
from time import sleep
bot = randint(0, 10)
tentativas = 1
pensa = 'PENSANDO...'
print('O computador esta pensando em um numero entre 0 e 10')
for x in pensa:
    print(x, end='')
    sleep(0.3)

palpite = int(input('\nQual seu palpite?\n>'))
while palpite != bot:
    if palpite > bot:
        palpite = int(input('Menos... tente novamente\n>'))
    else:
        palpite = int(input('Mais... tente novamente\n>'))
    tentativas += 1
print('Voce precisou de {} tentativas pra acertar. PARABENS!!!'.format(tentativas))

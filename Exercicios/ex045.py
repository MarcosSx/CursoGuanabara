# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from emoji import emojize
from random import choice
from time import sleep

cores = {
    'limpa': '\33[m',
    'vermelho': '\33[1;97;41m',
    'verde': '\33[1;97;42m',
    'azul': '\33[1;97;44m',
    'amarelo': '\33[1;97;43m'
}
mao = {
    'pedra': emojize(':oncoming_fist:'),
    'papel': emojize(':hand_with_fingers_splayed:'),
    'tesoura': emojize(':victory_hand:'),
    'empatou': emojize(':handshake:'),
    'derrota': emojize(':crying_face:'),
    'vitoria': emojize(':smiling_face_with_sunglasses:')
}
print('Bora jogar JOKENPÔ!!!\n{}{}{}{}'.format(' ' * 7, mao['papel'], mao['pedra'], mao['tesoura']))
opcoes = ['1', '2', '3']
bot = choice(opcoes)

jogador = str(input('Escolha uma opção:\n1 - pedra\n2 - papel\n3 - tesoura\n'))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('POO!!!')

if jogador == '1':
    if bot == jogador:
        print('{}EMPATE {}{}'.format(cores['amarelo'], mao['empatou'], cores['limpa']))
        bot = mao['pedra']
    elif bot == '2':
        print('{}VOCÊ PERDEU {}{}'.format(cores['vermelho'], mao['derrota'], cores['limpa']))
        bot = mao['papel']
    else:
        print('{}VOCÊ VENCEU {}{}\n{}PARABENS!!! {}{}{}{}'.format(cores['verde'], mao['vitoria'], cores['limpa'],
                                                                  cores['verde'], mao['pedra'], mao['papel'],
                                                                  mao['tesoura'], cores['limpa']))
        bot = mao['tesoura']
    jogador = mao['pedra']

elif jogador == '2':
    if bot == jogador:
        print('{}EMPATE {}{}'.format(cores['amarelo'], mao['empatou'], cores['limpa']))
        bot = mao['papel']
    elif bot == '3':
        print('{}VOCÊ PERDEU {}{}'.format(cores['vermelho'], mao['derrota'], cores['limpa']))
        bot = mao['tesoura']
    else:
        print('{}VOCÊ VENCEU {}{}\n{}PARABENS!!! {}{}{}{}'.format(cores['verde'], mao['vitoria'], cores['limpa'],
                                                                  cores['verde'], mao['pedra'], mao['papel'],
                                                                  mao['tesoura'], cores['limpa']))
        bot = mao['pedra']
    jogador = mao['papel']

elif jogador == '3':
    if bot == jogador:
        print('{}EMPATE {}{}'.format(cores['amarelo'], mao['empatou'], cores['limpa']))
        bot = mao['tesoura']
    elif bot == '1':
        print('{}VOCÊ PERDEU {}{}'.format(cores['vermelho'], mao['derrota'], cores['limpa']))
        bot = mao['pedra']
    else:
        print('{}VOCÊ VENCEU {}{}\n{}PARABENS!!! {}{}{}{}'.format(cores['verde'], mao['vitoria'], cores['limpa'],
                                                                  cores['verde'], mao['pedra'], mao['papel'],
                                                                  mao['tesoura'], cores['limpa']))
        bot = mao['papel']
    jogador = mao['tesoura']
else:
    print('OPÇÃO INVALIDA')
print('{}Você escolheu {} e o computador escolheu {}{}'.format(cores['azul'], jogador, bot, cores['limpa']))

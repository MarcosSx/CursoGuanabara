# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
while True:
    bot = randint(0, 10)
    n = int(input('Insira um numero: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    soma = n + bot
    if soma % 2 == 0:
        if escolha in 'P':
            print('Voce venceu')
            print(f'O computador escolheu Ímpar e jogou {bot} e voce escolheu Par e jogou {n} e a soma é {soma}')
            cont += 1
        else:
            print('Voce perdeu')
            print(f'O computador escolheu Par e jogou {bot} e voce escolheu Ímpar e jogou {n} e a soma é {soma}')
            break
    else:
        if escolha in 'I':
            print('Voce venceu')
            print(f'O computador escolheu Par e jogou {bot} e voce escolheu Ímpar e jogou {n} e a soma é {soma}')
            cont += 1
        else:
            print('Voce perdeu')
            print(f'O computador escolheu Ímpar e jogou {bot} e voce escolheu Par e jogou {n} e a soma é {soma}')
            break
print(f'FIM DE JOGO\nVoce ganhou {cont} vezes')

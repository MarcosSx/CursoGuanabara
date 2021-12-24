# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
             'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}

ranking = list()
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'    O {k} tirou {v}')
    sleep(0.3)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=-' * 10)
print('    ==RANKING DOS JOGADORES==')
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}')

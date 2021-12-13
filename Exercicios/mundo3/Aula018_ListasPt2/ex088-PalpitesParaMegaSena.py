# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta.
from time import sleep
from random import randint

jogos = list()
jogadas = list()
print('#-#' * 15)
print(f'{"MEGA DA VIRADA":^45}')
print('#-#' * 15)
quant = int(input('Quantos jogos deseja fazer? '))

for i in range(0, quant):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogadas:
            jogadas.append(num)
            cont += 1
        if cont >= 6:
            break
    jogadas.sort()
    jogos.append(jogadas[:])
    jogadas.clear()

print('$¨$' * 2, f'SORTEANDO {quant} JOGOS', '$¨$' * 2)
for pos, j in enumerate(jogos):
    print(f'Jogo {pos + 1}: {j}')
    sleep(0.5)
print('$¨$' * 2, f'{"BOA SORTE":^17}', '$¨$' * 2)

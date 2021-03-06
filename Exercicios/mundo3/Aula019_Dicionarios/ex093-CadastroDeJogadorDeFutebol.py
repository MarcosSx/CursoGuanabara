# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

nome = str(input('Nome do jogador: '))
tot_partidas = int(input(f'Quantas partidas {nome} jogou? '))
partidas = list()
for p in range(0, tot_partidas):
    partidas.append(int(input(f'  Quantos gols na partida {p + 1}? ')))
print('-=' * 30)
jogador = {'nome': nome, 'gols': partidas[:], 'total': sum(partidas)}
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for c, i in enumerate(jogador['gols']):
    print(f'    => Na partida {c + 1}, fez {i} gols')
print(f'Foi um total de {jogador["total"]} gols')

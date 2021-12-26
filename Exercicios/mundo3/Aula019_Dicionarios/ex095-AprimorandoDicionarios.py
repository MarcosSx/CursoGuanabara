# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
time = list()
partidas = list()
jogador = dict()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, tot_partidas):
        partidas.append(int(input(f'  Quantos gols na partida {p + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('ERRO! Digite S ou N.\nDeseja continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('-=' * 28)
print(f'cod {"nome":<20}{"gols":<20}{"total":<20}')
print('_' * 56)
for cont, i in enumerate(time):
    print(f'{cont:>3} ', end='')
    for v in i.values():
        print(f'{str(v):<20}', end='')
    print()
print('_' * 56)
while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp < len(time):
        print(f' --LEVANTAMENTO DO JOGADOR {time[resp]["nome"]}')
        for pos, g in enumerate(time[resp]['gols']):
            print(f'    No jogo {pos + 1} fez {g} gols.')
    elif resp == 999:
        break
    else:
        print(f'ERRO! Não exite jogador com codigo {resp}!')



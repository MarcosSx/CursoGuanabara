# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o
# nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols='0'):
    nome = '<desconhecido>' if nome in '' else nome
    gols = '0' if gols in '' else gols
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))
print(ficha(nome, gols))

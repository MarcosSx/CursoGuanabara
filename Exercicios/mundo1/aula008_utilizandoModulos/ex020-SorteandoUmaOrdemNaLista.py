# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

aluno1 = str(input('Digite seu nome:\n'))
aluno2 = str(input('Digite seu nome:\n'))
aluno3 = str(input('Digite seu nome:\n'))
aluno4 = str(input('Digite seu nome:\n'))

alunos = [aluno4, aluno3, aluno2, aluno1]
shuffle(alunos)
print('A ordem de apresentação dos trabalhos é')
print(alunos)
# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

aluno1 = str(input('Digite seu nome:\n'))
aluno2 = str(input('Digite seu nome:\n'))
aluno3 = str(input('Digite seu nome:\n'))
aluno4 = str(input('Digite seu nome:\n'))

alunos = [aluno4, aluno3, aluno2, aluno1]
escolhido = choice(alunos)
print('Aluno sorteado: {}'.format(escolhido))

# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

numero = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
print(f'Os numeros gerados foram {numero}, o menor valor é {min(numero)} e o maior valor é {max(numero)}')

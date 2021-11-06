# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

contMaiores = 0
contMenores = 0

for i in range(1, 8, 1):
    ano = int(input('Digite o ano em que nasceu: '))
    idade = date.today().year - ano

    if idade >= 18:
        contMaiores += 1
    else:
        contMenores += 1
print('menores {}'.format(contMenores))
print('maiores {}'.format(contMaiores))

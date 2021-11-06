# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.
nome = str(input('Insira seu nome aqui:\n>>> ')).strip()
n = nome.split()
print('Muito prazer {} {}'.format(n[0], n[len(n) - 1]))

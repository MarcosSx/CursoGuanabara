# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite seu salario: R$ '))
aumento = salario * 15 / 100
print('Seu salario com aumento de 15% é de R${:.2f}'.format(salario + aumento))
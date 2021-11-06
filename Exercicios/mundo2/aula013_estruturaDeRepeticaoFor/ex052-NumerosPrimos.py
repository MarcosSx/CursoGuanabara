# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Insira um numero inteiro para saber se ele é primo: '))
total = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')
print('\033[m\nO numero foi {} divisivel {} vezes'.format(numero, total))
if total == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')

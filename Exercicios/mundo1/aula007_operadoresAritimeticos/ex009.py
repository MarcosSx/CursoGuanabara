# Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um numero para obter sua taboada: '))
i = 0
print('A taboada do {} é'.format(n))
print('*' * 13)
for i in range(11):
    print('{} x {:<2} = {}'.format(n, i, n * i))
    i = i + 1
print('*' * 13)

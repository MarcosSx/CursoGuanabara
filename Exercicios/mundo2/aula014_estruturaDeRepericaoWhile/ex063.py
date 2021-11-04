# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci.

n = int(input('Digite a quantidade de termos que deseja ver na sequencia de Fibonacci: '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end=' - ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3, end=' - ')
    cont += 1
    t1 = t2
    t2 = t3
print('FIM')

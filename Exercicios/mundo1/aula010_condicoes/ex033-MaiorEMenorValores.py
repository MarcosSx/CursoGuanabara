# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite um numero\n'))
b = int(input('Digite um numero\n'))
c = int(input('Digite um numero\n'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior numero digitado foi:\n>{}\nO menor numero digitado foi:\n>{}'.format(maior, menor))
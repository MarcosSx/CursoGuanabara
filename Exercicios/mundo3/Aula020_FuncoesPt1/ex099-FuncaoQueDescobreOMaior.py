# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*num):
    print('Analizando os valores passados...')
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) > 0:
        print(f'O maior valor informado foi {max(num)}')


maior(1, 2, 5, 7)
maior(2, 5, 0)
maior(5, 7)
maior(0)
maior()

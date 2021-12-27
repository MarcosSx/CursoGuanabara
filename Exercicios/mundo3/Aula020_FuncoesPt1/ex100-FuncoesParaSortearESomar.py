# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.
from random import randint


def sorteia(lista):
    print('Sorteando os 5 valores da lista: ', end='')
    for i in range(0, 5):
        numeros = randint(0, 9)
        print(numeros, end=' ')
        lista.append(numeros)
    print('PRONTO!')


def somaPar(lst):
    print(f'Somando os valores pares de {lst}, temos ', end='')
    pares = 0
    for i in lst:
        if i % 2 == 0:
            pares += i
    print(pares)


lista = list()
sorteia(lista)
somaPar(lista)

# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if passo < 0:
        passo *= -1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.3)
        print()
        print('=-' * 20)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
            sleep(0.3)
        print()
        print('=-' * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

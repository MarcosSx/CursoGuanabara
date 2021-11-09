# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = list()
maior = menor = 0
for p in range(0, 5):
    numeros.append(int(input(f'Digite um numero para a posição {p}: ')))
print(f'Lista de numeros: {numeros}')
print(f'O maior valor é {max(numeros)} e esta na posição: ', end='')
for i, val in enumerate(numeros):
    if val == max(numeros):
        print(f'{i}...', end='')
print(f'\nO menor valor é {min(numeros)} e esta na posição: ', end='')
for i, val in enumerate(numeros):
    if val == min(numeros):
        print(f'{i}...', end='')

# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    parar = ' '
    while parar not in 'SN':
        parar = input('Deseja continuar? [S/N] ').strip()[0].upper()

    if parar in 'N':
        break

lista.sort(reverse=True)
print(f'Voce digitou {len(lista)} numeros')
print(f'Os numeros digitados em ordem decrescente são: {lista}')
print(f'O numero 5 foi encontrado na lista' if lista.count(5) > 0 else f'O numero 5 não foi encontrado na lista')

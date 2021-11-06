# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
# peso lidos.
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    else:
        menor = peso

print('maior {}, menor {}'.format(maior, menor))

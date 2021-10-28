# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
# ela pode comprar.

carteira = float(input('Digite o valor que tem na carteira para verificar quantos dolares pode comprar: R$ '))
cotDolar = float(5.65)

print('Voce tem {:.2f} reais e pode comprar {:.2f} dolares'.format(carteira, carteira / cotDolar))

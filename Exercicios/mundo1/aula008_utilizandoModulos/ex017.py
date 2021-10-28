# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

catOposto = float(input('Insira o valor do cateto oposto\n>>> '))
catAdja = float(input('Insira o valor do cateto adjacente\n>>> '))
print('O valor da hipotenusa deste triangulo com cateto oposto {} e cateto adjacente {} é igual a {:.4f}'.format(
    catOposto, catAdja, math.hypot(catAdja, catOposto)))

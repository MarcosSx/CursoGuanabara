# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

angulo = float(input('Digite qualquer angulo: '))
print('Valores dos calculos do angulo {:.2f}:\nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(
    angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))

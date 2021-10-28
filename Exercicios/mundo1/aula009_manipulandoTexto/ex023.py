# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input('Insira um numero de 0 a 9999\n'))
milhares = numero // 1000
centenas = numero % 1000 // 100
dezenas = numero % 1000 % 100 // 10
unidades = numero % 1000 % 100 % 10 // 1
print('O numero {} possui:\nMilhares {}\nCentenas {}\nDezenas {}\nUnidades {}\n\n'.format(numero, milhares, centenas, dezenas, unidades))
#Resolução Gunabara
# n = str(numero)
# print('O numero {} possui:\nMilhares {}\nCentenas {}\nDezenas {}\nUnidades {}'.format(numero, n[0], n[1], n[2], n[3]))
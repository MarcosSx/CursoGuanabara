# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja
# errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while sexo != 'F' and sexo != 'M':
    print('{} não é um sexo valido!!'.format(sexo))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    sexo = sexo

print('Voce digitou {}, sexo valido'.format(sexo))

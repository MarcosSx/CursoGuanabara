# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
mediaIdade = 0
somaIdade = 0
maisVelho = 0
nomeMaisVelho = ''
quantMulher = 0
for pessoa in range(1, 5):
    print('-*-' * 15)
    nome = str(input('Digite o nome da pessoa: '))
    idade = float(input('Digite o idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa (M)/(F): '))
    if pessoa == 1 and sexo in 'Mm':
        maisVelho = idade
    if sexo in 'Mm' and idade > maisVelho:
        maisVelho = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        quantMulher += 1
    print('-*-' * 15)
    somaIdade += idade
mediaIdade = somaIdade / 4
print('A meida de idade do grupo é de {}'.format(mediaIdade))
print('O homem mais velho é {} com {} anos'.format(nomeMaisVelho, maisVelho))
print('A quantidade de mulheres abaixo de 20 anos é de {}'.format(quantMulher))

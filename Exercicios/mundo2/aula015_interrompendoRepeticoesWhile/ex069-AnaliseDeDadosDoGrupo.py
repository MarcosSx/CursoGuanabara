# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
# programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
maior = homens = menor = 0
while True:
    print('-' * 35)
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo da pessoa [F/M]: ')).strip().upper()[0]
    print('-' * 30)
    if idade >= 18:
        maior += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        menor += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(
    f'Foram cadastradas:\n{maior} pessoas maiores de 18 anos\n{homens} são homens\n{menor} mulheres menores de 20 anos')

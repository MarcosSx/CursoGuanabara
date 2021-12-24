# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
dados = list()
pessoas = dict()

while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('ERRO! Por favor, digite apenas F ou M\nSexo: ')).strip().upper()[0]
    pessoas['Sexo'] = sexo
    pessoas['Idade'] = int(input('Idade: '))

    dados.append(pessoas.copy())

    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('ERRO! Responda apenas S ou N\nDeseja continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas')

soma_idade = 0
for i in dados:
    soma_idade += i['Idade']
media_idade = soma_idade / len(dados)
print(f'B) A média de idade é de {media_idade:.2f} anos')

print(f'C) As mulheres cadastradas foram ', end='')
for i in dados:
    if i['Sexo'] == 'F':
        print(f'{i["Nome"]} ', end='')
print()

print(f'D) Lista de pessoas que estão acima da média:')
for i in dados:
    if i['Idade'] > media_idade:
        print('    ', end='')
        for k, v in i.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')

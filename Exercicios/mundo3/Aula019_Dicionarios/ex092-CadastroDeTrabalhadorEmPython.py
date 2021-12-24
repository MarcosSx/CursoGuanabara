# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
# (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
hoje = datetime.now().year
nome = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
ctps = int(input('CTPS: '))
pessoas = {'Nome': nome, 'Idade': hoje - ano, 'CTPS': ctps}
if pessoas['CTPS'] != 0:
    pessoas['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoas['Salario'] = float(input('Salario: '))
    pessoas['Aposentadoria'] = ((pessoas['Ano de contratação'] + 35) - hoje) + pessoas['Idade']


for k, v in pessoas.items():
    print(f'    -{k} tem o valor {v}')
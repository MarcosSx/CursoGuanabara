# Exercício Python 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {'Nome': str(input('Nome: '))}
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Em recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print()
for k, v in aluno.items():
    print(f'{k} é igual a {v}')



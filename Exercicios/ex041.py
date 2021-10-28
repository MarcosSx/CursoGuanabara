# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

anoNasc = int(input('Insira o ano de nascimento do atleta para saber sua categoria\n>>'))
anoAtual = date.today().year

idade = anoAtual - anoNasc

if anoAtual >= anoNasc >= 1900:
    if idade <= 9:
        print('Atleta categoria MIRIM')
    elif idade <= 14:
        print('Atleta categoria INFANTIL')
    elif idade <= 19:
        print('Atleta categoria JUNIOR')
    elif idade <= 25:
        print('Atleta categoria SÊNIOR')
    else:
        print('Atleta categoria MASTER')
else:
    print('Ano invalido')

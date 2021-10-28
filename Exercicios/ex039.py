# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoNas = int(input('Digite o ano que nasceu?\n'))
idade = date.today().year - anoNas

if idade > 18:
    alistou = str(input('Ja se alistou-se no EB (S) ou (N)?\n')).upper()

    if alistou == 'N':
        passou = idade - 18
        print('Sua idade é {}\nVoce ja passou da idade para se alistar.\nEstá {} ano(s) atrasado'.format(idade, passou))
        print('Seu ano de alistamento foi em {}'.format(date.today().year - passou))

    elif alistou == 'S':
        print('Obrigado pela informação')

    else:
        print('Opção invalida')

elif idade == 18:
    print('Sua idade é {}\nVoce deve alistar-se este ano'.format(idade))

else:
    falta = 18 - idade
    print('Sua idade é {}\nVoce deve se alistar daqui {} anos em {}'.format(idade, falta, falta + date.today().year))

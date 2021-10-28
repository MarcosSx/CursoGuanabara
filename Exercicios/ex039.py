# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#todo
import datetime
diaNascimento = int(input('Digite o dia que nasceu'))
mesNascimento = int(input('Digite o mes que nasceu'))
anoNascimento = int(input('Digite o ano que nasceu'))
print('Voce nasceu em {}/{}/{}'.format(diaNascimento, mesNascimento, anoNascimento))
print(datetime.date.strftime())
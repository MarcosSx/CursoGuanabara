# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 30)
print('-{:^28}-'.format('Banco senta aqui'))
print('=' * 30)
saque = int(input('Qual valor deseja sacar: R$'))
total = saque
cedula = 50
totCed = 0
while True:
    if total >= cedula:
        total -= cedula
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cedulas de R${cedula:.2f} ')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCed = 0
        if total == 0:
            break
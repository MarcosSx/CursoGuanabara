# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

sair = 0
num1 = float(input('Digite o 1º numero: '))
num2 = float(input('Digite o 2º numero: '))
while sair != 5:
    print('-=-' * 12)
    print('[ 1 ] somar | [ 2 ] multiplicar\n[ 3 ] maior | [ 4 ] novos números\n[ 5 ] sair do programa')
    opcao = int(input('Digite uma opção: '))
    if opcao != 5 and opcao < 5:
        if opcao == 1:
            print('[ 1 ] somar\nA soma dos numeros {} e {} é igual a {}\n'.format(num1, num2, num1 + num2))
        elif opcao == 2:
            print('[ 2 ] multiplicar\nMultiplicando os numeros {} e {} é igual a {}'.format(num1, num2, num1 * num2))
        elif opcao == 3:
            print('[ 3 ] maior\nVoce digitou os numeros {} e {} e o maior é {}'.format(num1, num2,
                                                                                       num1 if num1 > num2 else num2))
        elif opcao == 4:
            print('[ 4 ] limpar números\nDigite novos numeros')
            num1 = float(input('Digite o 1º numero: '))
            num2 = float(input('Digite o 2º numero: '))
        else:
            print('Voce digitou {}\nOPÇÃO INVALIDA'.format(opcao))
    elif opcao == 5:
        sair = opcao
        print('Finalizando programa...')
    else:
        print('Voce digitou {}\nOPÇÃO INVALIDA'.format(opcao))

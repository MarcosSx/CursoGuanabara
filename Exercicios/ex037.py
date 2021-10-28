# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
# todo converter para bases
numero = float(input('Digite um numero para ser convertido\n>'))
print('Você quer converter o numero {:.0f} para:'.format(numero))
opcoes = int(input('1 - BINARIO\n2 - OCTAL\n3 - HEXADECIMAL\n>'))
converterBin = numero // 2
if opcoes == 1:
    print('Convertendo {:.0f} para BINARIO teremos '.format(numero))
elif opcoes == 2:
    print('Convertendo {:.0f} para OCTAL teremos '.format(numero))
elif opcoes == 3:
    print('Convertendo {:.0f} para HEXADECIMAL teremos '.format(numero))
else:
    print('Opção invalida')

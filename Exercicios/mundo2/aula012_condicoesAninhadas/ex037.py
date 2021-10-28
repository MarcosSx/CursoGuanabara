# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um numero para ser convertido\n>'))
print('Você quer converter o numero {:.0f} para:'.format(numero))
opcoes = int(input('1 - BINARIO\n2 - OCTAL\n3 - HEXADECIMAL\n>'))

if opcoes == 1:
    print('Convertendo...\nO numero {:.0f} em BINARIO é {}'.format(numero, bin(numero)[2:]))
elif opcoes == 2:
    print('Convertendo...\nO numero {:.0f} em OCTAL é {}'.format(numero, oct(numero)[2:]))
elif opcoes == 3:
    print('Convertendo...\nO numero {:.0f} em HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida')

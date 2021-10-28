# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
#
num1 = int(input('Digite o primeiro numero:\n'))
num2 = int(input('Digite o segundo numero:\n'))
cores = {'limpa': '\33[m',
         'azul': '\33[1;30;44m',
         'verde': '\33[1;30;42m',
         'vermelho': '\33[1;30;41m'}

if num1 > num2:
    print('{} é {}MAIOR{} que {}'.format(num1, cores['verde'], cores['limpa'], num2))
elif num1 < num2:
    print('{} é {}MENOR{} que {}'.format(num1, cores['vermelho'], cores['limpa'], num2))
else:
    print('{} e {} são {}IGUAIS{}'.format(num1, num2, cores['azul'], cores['limpa']))

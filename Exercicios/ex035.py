# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.
print('Digite as retas do tiangulo:')
a = float(input('\33[1;30;43mDigite o tamanho do lado a:\33[m\n'))
b = float(input('\33[1;30;44mDigite o tamanho do lado b:\33[m\n'))
c = float(input('\33[1;30;45mDigite o tamanho do lado c:\33[m\n'))

if a < b + c and b < a + c and c < a + b:
    print('\33[1;30;42mVocê formou um triangulo!!!\33[m')
else:
    print('\33[1;30;41mVocê não conseguiu formar um triangulo!!!\33[m')

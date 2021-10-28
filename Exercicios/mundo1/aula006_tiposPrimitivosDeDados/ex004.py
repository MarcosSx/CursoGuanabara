# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

varA = input('Digite algo:')
print('O tipo primitivo desse valor é: ', type(varA))
print('as informações do que digitou é alfa? {}, {}, {}, {},'.format(varA.isalpha(), varA.isalnum(), varA.isascii(),
                                                                     varA.isdigit()))

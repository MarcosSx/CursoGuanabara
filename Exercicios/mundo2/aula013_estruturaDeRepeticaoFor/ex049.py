# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for.

num = float(input('Digite um numero para saber sua tabuada\n>'))
for i in range(1, 11):
    print('{} x {:<2} = {}'.format(num, i, num * i))
    i = i + 1

# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por Km rodado.
kmsPercorridos = float(input('Quantos kilometros percorreu com o carro?\n>>> '))
diasAlugado = int(input('Por quantos dias o carro esteve alugado?\n>>> '))
valorAluguel = (kmsPercorridos * 0.15) + (diasAlugado * 60)
print('Valor a pagar: R${:.2f}'.format(valorAluguel))
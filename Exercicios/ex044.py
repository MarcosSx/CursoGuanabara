# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Qual o valor do produto?\nR$'))
print('Escolha uma forma de pagamento:\n1 - À vista dinheiro/cheque\n2 - À vista no cartão\n', end='')
print('3 - Crédito em ate 2x\n4 - Crédito 3x ou mais')
pagamento = int(input('Qual a forma escolhida?\n>'))
if pagamento == 1:
    pagar = preco - (preco * 0.1)
    print(pagar)
elif pagamento == 2:
    pagar = preco - (preco * 0.05)
    print(pagar)
elif pagamento == 3:
    print(preco)
elif pagamento == 4:
    pagar = preco + (preco * 0.2)
    print(pagar)
else:
    print('Opção invalida')

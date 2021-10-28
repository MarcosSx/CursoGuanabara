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
    print('''Opção escolhida [-1-] À vista dinheiro/cheque
Você recebeu um desconto de 10% e de R${:.2f} ira pagar R${:.2f}'''.format(preco, pagar))

elif pagamento == 2:
    pagar = preco - (preco * 0.05)
    print('''Opção escolhida [-2-] À vista no cartão
Você recebeu um desconto de 5% e de R${:.2f} ira pagar R${:.2f}'''.format(preco, pagar))

elif pagamento == 3:
    print('''Opção escolhida [-3-] Crédito em ate 2x
Você ira pagar R${:.2f} em 2x R${:.2f} SEM JUROS'''.format(preco, preco / 2))

elif pagamento == 4:
    parcelas = int(input('Opção escolhida [-4-] Crédito 3x ou mais\nVai ser parcelado em quantas vezes?\n'))

    if parcelas >= 3:
        pagar = preco + (preco * 0.2)
        print('''Você ira pagar R${:.2f} em {}x R${:.2f} COM 20% DE JUROS'''.format(pagar / parcelas, parcelas, pagar))

    else:
        print('Opção invalida')

else:
    print('Opção invalida')

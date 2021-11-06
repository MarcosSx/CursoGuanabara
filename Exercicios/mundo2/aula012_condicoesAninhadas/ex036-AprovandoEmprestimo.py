# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado

valorDaCasa = float(input('Qual o valor da casa desejada?\n>>>R$ '))
salario = float(input('Qual o salario do comprador?\n>>>R$ '))
anos = int(input('Em quantos anos o comprador deseja liquidar o pagamento?\n>>> '))
prestacoes = anos * 12

valorPrestacao = valorDaCasa / prestacoes

aprovaImprestimo = salario * 0.3

print('Para pagar uma casa no valor de R${:.2f} em {} anos, '.format(valorDaCasa, anos), end='')
print('as prestações serão no valor de R${:.2f}'.format(valorPrestacao))

if aprovaImprestimo <= valorPrestacao:
    print('O emprestimo foi negado')
else:
    print('O emprestimo foi aprovado')

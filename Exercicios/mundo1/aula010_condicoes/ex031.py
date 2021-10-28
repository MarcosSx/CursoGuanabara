# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas
distancia = float(input('Qual a distancia da sua viagem meu parça?\n'))
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('preco da passagem é igual a {:.2f}'.format(preco))
if distancia <= 200:
    passagem = 0.5 * distancia
    print('Mermao a passagem ta R$0.50 e ce vai pagar R${:.2f}'.format(passagem))
else:
    passagem = 0.45 * distancia
    print('Parça, como ce vai mais longe a passagem pra voce ta R$0.45 e ce vai pagar R${:.2f}'.format(passagem))

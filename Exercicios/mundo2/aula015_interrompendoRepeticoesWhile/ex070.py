# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = quant = cont = 0
loja = 'LOJA DO MARCÃO'
print('-@-' * 15)
print(f'{loja:^45}')
print('-@-' * 15)
while True:
    print('-' * 50)
    nome = str(input('Nome do produto: >>>'))
    preco = float(input('Digite o valor do produto: R$'))
    print('-' * 50)
    total += preco
    cont += 1
    if preco > 1000:
        quant += 1
    if cont == 1:
        barato = preco
        produto = nome
    if barato > preco:
        barato = preco
        produto = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto é de R${total:.2f}, {quant} custaram mais de R$1000.00 e o produto mais barato foi {produto}')


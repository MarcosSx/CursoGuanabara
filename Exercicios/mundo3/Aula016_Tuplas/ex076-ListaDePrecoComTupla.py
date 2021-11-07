# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
# sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular
produtos = 'Arroz', 10, 'Feijao', 5, 'Carne', 20, 'Manteiga', 3, 'Batata', 5, 'Frango', 19.9
print('_' * 50)
print(f'{"LISTA DE PREÇOS":^50}')
print('_' * 50)
for p in range(len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<40}', end='')
    else:
        print(f'R${produtos[p]:>8.2f}')
print('_' * 50)

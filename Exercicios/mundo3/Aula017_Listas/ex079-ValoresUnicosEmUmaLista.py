# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista = list()

while True:
    numero = int(input('Digite um numero: '))

    if numero in lista:
        print(f'O numero {numero} já foi digitado')
    else:
        lista.append(numero)

    parar = ' '
    while parar not in 'SN':
        parar = input('Deseja parar [S/N]: ').upper().strip()[0]
    if parar in 'S':
        break

print(sorted(lista))

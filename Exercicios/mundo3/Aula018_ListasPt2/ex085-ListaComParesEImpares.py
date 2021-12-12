# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
# crescente.

# Solução Guanabara
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')

# Minha solução
# valores = list()
#
# for i in range(1, 8):
#     valores.append(int(input(f'Digite o {i}º valor: ')))
#
# print('Os valores pares digitados foram: ', end='')
# for v in sorted(valores):
#     if v % 2 == 0:
#         print(f'{v}', end=' ')
#
# print('\nOs valores impares digitados foram: ', end='')
# for v in sorted(valores):
#     if v % 2 != 0:
#         print(f'{v}', end=' ')

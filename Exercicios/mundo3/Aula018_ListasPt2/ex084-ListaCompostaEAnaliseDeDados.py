# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,
# mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Resolução Guanabara

# pessoas = list()
# dados = list()
# mais_pesado = mais_leve = 0
#
# while True:
#     dados.append(str(input('Nome: ')))
#     dados.append(int(input('Peso: ')))
#     if len(pessoas) == 0:
#         mais_leve = mais_pesado = dados[1]
#     else:
#         if dados[1] > mais_pesado:
#             mais_pesado = dados[1]
#         if dados[1] < mais_leve:
#             mais_leve = dados[1]
#     pessoas.append(dados[:])
#     dados.clear()
#
#     parar = ' '
#     while parar not in 'SN':
#         parar = str(input('Deseja parar? [S/N]')).strip()[0].upper()
#
#     if parar in 'S':
#         break
#
# print(f'Ao t odo, você cadastrou {len(pessoas)} pessoas')
# print(f'O maior peso foi de {mais_pesado}Kg. Peso de ', end='')
# for p in pessoas:
#     if p[1] == mais_pesado:
#         print(f'[{p[0]}] ', end='')
# print()
# print(f'O menor peso foi de {mais_leve}Kg. Peso de ', end='')
# for p in pessoas:
#     if p[1] == mais_leve:
#         print(f'[{p[0]}] ', end='')
# print()

# Minha resolução

pessoas = list()
dados = list()
pesado = list()
leve = list()
mais_pesado = mais_leve = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))

    pessoas.append(dados[:])
    dados.clear()

    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja parar? [S/N]')).strip()[0].upper()

    if parar in 'S':
        break

print(f'Ao t odo, você cadastrou {len(pessoas)} pessoas')

for pos, p in enumerate(pessoas):
    if p[1] >= 70:
        pesado.append(pessoas[pos][0])
        if mais_pesado == 0:
            mais_pesado = pessoas[pos][1]
        elif mais_pesado < pessoas[pos][1]:
            mais_pesado = pessoas[pos][1]
    elif p[1] <= 50:
        leve.append(pessoas[pos][0])
        if mais_leve == 0:
            mais_leve = pessoas[pos][1]
        elif mais_leve > pessoas[pos][1]:
            mais_leve = pessoas[pos][1]


print(f'O maior peso foi de {mais_pesado} Kg. Peso de {pesado}')
print(f'O menor peso foi de {mais_leve} Kg. Peso de {leve}')

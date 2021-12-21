# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tot_par = ter_col = mai_seg = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))

for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            tot_par += matriz[i][j]

for m in range(0, 3):
    if matriz[1][m] > mai_seg:
        mai_seg = matriz[1][m]

for n in range(0, 3):
    ter_col += matriz[n][2]

print('*-*' * 15)
for li in range(0, 3):
    for co in range(0, 3):
        print(f'[{matriz[li][co]:^6}]', end='')
    print()
print(f'A soma de todos os valores pares digitados é {tot_par}')
print(f'A soma dos valores da terceira coluna {ter_col}')
print(f'O maior valor da segunda linha é {mai_seg}')

# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while

num = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão dessa PA: '))
print('PA = {}'.format(num), end=' → ')
decimo = num + (10 - 1) * razao
while num != decimo:
    pa = num + razao
    print(pa, end=' → ')
    num += razao
print('Fim')
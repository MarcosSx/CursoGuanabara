# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while
# Resolução Guanabara

print('Gerador de PA')
print('-=' * 10)
# primeiro = int(input('Primeiro termo: '))
# razão = int(input('Razão da PA: '))
# termo = primeiro
# cont = 1
# while cont <= 10:
#     print('{} → '.format(termo), end='')
#     termo += razão
#     cont += 1
# print('FIM')

num = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão dessa PA: '))
print('PA = {}'.format(num), end=' → ')
decimo = num + (10 - 1) * razao
while num != decimo:
    pa = num + razao
    print(pa, end=' → ')
    num += razao
print('Fim')

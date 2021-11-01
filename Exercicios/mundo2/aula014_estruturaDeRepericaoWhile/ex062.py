# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O
# programa encerrará quando ele disser que quer mostrar 0 termos.

num = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão dessa PA: '))
quant = int(input('Digite quantos termos deseja ver: '))
termos = num + (quant - 1) * razao
print('PA = {}'.format(num), end=' → ')
while num != termos:
    pa = num + razao
    print(pa, end=' → ')
    num += razao
    if num == termos:
        quant = int(input('\nDigite quantos mais termos deseja ver: '))
        termos = num + (quant - 1) * razao
        print('PA = {}'.format(num), end=' → ')
        if quant == 0:
            termos = num
print('Fim')

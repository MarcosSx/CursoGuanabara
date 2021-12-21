from random import randint

cnpj = list()
# gera 12 numeros aleatorios e adiciona na lista cnpj xx.xxx.xxx/xxxx
for i in range(0, 12):
    if len(cnpj) < 8:
        cnpj.append(randint(0, 9))
    elif len(cnpj) < 11:
        cnpj.append(0)
    else:
        cnpj.append(1)
# gera os dois ultimos digitos e adiciona ao cnpj xx.xxx.xxx.xxx/xxxx-xx
for i in range(2):
    contb1 = len(cnpj) - 7
    contb2 = 9
    soma = 0
    for n in range(len(cnpj)):
        if n < len(cnpj) - 8:
            soma += cnpj[n] * contb1
            contb1 -= 1
        else:
            soma += cnpj[n] * contb2
            contb2 -= 1
    if soma % 11 < 2:
        cnpj.append(0)
    else:
        cnpj.append(11 - (soma % 11))
cnpjFormatado = '%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d' % tuple(cnpj)
print(cnpjFormatado)



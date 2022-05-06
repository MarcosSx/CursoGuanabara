from random import randint


def cpf_generator(pontuado=True):
    cpf = list()
    # gera 9 numeros aleatorios e adiciona na lista cpf xxx.xxx.xxx
    for num in range(0, 9):
        cpf.append(randint(0, 9))
    # gerar os dois ultimos digitos e adiciona ao cpf xxx.xxx.xxx-xx
    for i in range(0, 2):
        quant = len(cpf) + 1
        soma = 0
        for n in cpf:
            soma += n * quant
            quant -= 1
        if soma % 11 < 2:
            cpf.append(0)
        else:
            cpf.append(11 - (soma % 11))

    if pontuado:
        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)
    else:
        return '%s%s%s%s%s%s%s%s%s%s%s' % tuple(cpf)


def cnpj_generator(pontuado=True):
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

    if pontuado:
        return '%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d' % tuple(cnpj)
    else:
        return '%d%d%d%d%d%d%d%d%d%d%d%d%d%d' % tuple(cnpj)


print(cpf_generator(False))
print(cnpj_generator(False))

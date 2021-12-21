from random import randint

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
cpfFormatado = '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)
print(cpfFormatado)

cpfFormatado = cpfFormatado.replace('.', '').replace('-', '')
print(cpfFormatado)


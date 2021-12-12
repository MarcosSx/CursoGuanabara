from random import randint

cpf = list()
for num in range(0, 9):
    cpf.append(randint(0, 9))
# gerar o primeiro e segundo digito
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
print('%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf))
    
from random import randint


def cpf_cnpj_numbers_generator(type):
    generic_cpf_cnpj = []
    if type.upper() == 'CPF':
        for num in range(0, 9):
            generic_cpf_cnpj.append(randint(0, 9))
    elif type.upper() == 'CNPJ':
        for i in range(0, 12):
            if len(generic_cpf_cnpj) < 8:
                generic_cpf_cnpj.append(randint(0, 9))
            elif len(generic_cpf_cnpj) < 11:
                generic_cpf_cnpj.append(0)
            else:
                generic_cpf_cnpj.append(1)
    return generic_cpf_cnpj


def validator_digit_generator(numbers):
    sum_digits = 0
    for i, j in enumerate(reversed(numbers), start=2):
        if len(numbers) < 12:
            sum_digits += i * j
        else:
            if i <= 9:
                sum_digits += i * j
            else:
                sum_digits += (i - 8) * j
    cpf_cnpj_dv = abs(sum_digits % 11 - 11)
    if sum_digits % 11 < 2:
        cpf_cnpj_dv = 0
    return cpf_cnpj_dv


def formatter(doc, formatted=True):
    formatted_doc = ''
    if formatted:
        if len(doc) <= 12:
            formatted_doc = '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(doc)
        else:
            formatted_doc = '%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d' % tuple(doc)
    else:
        for i in doc:
            formatted_doc += str(i)
    return formatted_doc


def cpf_cnpj_generator(type, formatted=False):
    cpf_cnpj = cpf_cnpj_numbers_generator(type.upper())
    cpf_cnpj.append(validator_digit_generator(cpf_cnpj))
    cpf_cnpj.append(validator_digit_generator(cpf_cnpj))
    return formatter(cpf_cnpj, formatted)


print(cpf_cnpj_generator('cpf', True))
print(cpf_cnpj_generator('cnpj', True))

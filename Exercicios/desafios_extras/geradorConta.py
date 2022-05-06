import math
from random import randint


def generic_agency():
    agency = list()
    for i in range(0, 4):
        agency.append(randint(0, 9))
    return agency


def banco_do_brazil():
    agency = generic_agency()
    account = list()

    sum_agency_dv = 0
    for i, j in enumerate(reversed(agency), start=2):
        n = i * j
        sum_agency_dv += n

    agency_dv = abs((sum_agency_dv % 11) - 11)
    if agency_dv == 11 or agency_dv == 10:
        agency_dv = 0 if agency_dv == 10 else 'X'

    for i in range(0, 8):
        account.append(randint(0, 9))

    sum_account_dv = 0
    for i, j in enumerate(reversed(account), start=2):
        n = i * j
        sum_account_dv += n

    account_dv = abs((sum_account_dv % 11) - 11)
    if account_dv == 11 or account_dv == 10:
        account_dv = 0 if account_dv == 10 else 'X'

    agency_formatted = f'AG: %s%s%s%s-{agency_dv}\n' % tuple(agency)
    account_formatted = f'CC: %s%s%s%s%s%s%s%s-{account_dv}' % tuple(account)
    # print(agency_formatted + account_formatted)
    return f'{agency_formatted}{account_formatted}'


def citibank():
    agency = generic_agency()
    account = [0, 0, 0]

    for i in range(0, 7):
        account.append(randint(0, 9))

    sum_account_dv = 0
    for i, j in enumerate(reversed(account), start=2):
        n = i * j
        sum_account_dv += n

    account_dv = abs((sum_account_dv % 11) - 11)
    if account_dv == 11 or account_dv == 10:
        account_dv = 0

    agency_formatted = f'AG: %s%s%s%s\n' % tuple(agency)
    account_formatted = f'CC: %s%s%s%s%s%s%s%s%s%s-{account_dv}' % tuple(account)
    # print(agency_formatted + account_formatted)
    return f'{agency_formatted}{account_formatted}'


def itau():
    account = list()

    for i in range(0, 9):
        account.append(randint(0, 9))

    sum_account_dv = 0
    for i, j in enumerate(account):
        if i % 2 == 0:
            par = j * 2
            if par > 9:
                sum_account_dv += (par % 10) + math.floor(par / 10)
            else:
                sum_account_dv += par
        else:
            sum_account_dv += j

    account_dv = abs((sum_account_dv % 10) - 10)
    if sum_account_dv % 10 == 0:
        account_dv = 0

    account_formatted = f'AG: %s%s%s%s\nCC: %s%s%s%s%s-{account_dv}' % tuple(account)
    # print(account_formatted)
    return account_formatted


def caixa():
    agency = generic_agency()
    # tipo de conta corrente pf 001
    account = [0, 0, 1]

    for i in range(0, 12):
        if i < 4:
            account.insert(0, agency[i])
        else:
            account.append(randint(0, 9))

    sum_account_dv = 0
    for i, j in enumerate(reversed(account), start=2):
        if i <= 9:
            sum_account_dv += i * j
        else:
            sum_account_dv += (i - 8) * j

    account_dv = abs((math.floor(((sum_account_dv * 10) / 11)) * 11) - (sum_account_dv * 10))
    if account_dv == 10:
        account_dv = 0

    account_formatted = f'AG: %s%s%s%s\nCC: %s%s%s%s%s%s%s%s%s%s%s-{account_dv}' % tuple(account)
    # print(account_formatted)
    return account_formatted


def santander():
    multipliers = [9, 7, 3, 1, 9, 7, 1, 3, 1, 9, 7, 3]
    agency = reversed(generic_agency())
    account = list()

    for i in agency:
        account.insert(0, i)

    for i in range(0, 8):
        account.append(randint(0, 9))

    sum_dv = 0
    for i in range(len(multipliers)):
        sum_dv += (multipliers[i] * account[i]) % 10

    account_dv = abs(sum_dv % 10 - 10)
    if sum_dv % 10 == 0:
        account_dv = 0

    account_formatted = f'AG: %s%s%s%s\nCC: %s%s%s%s%s%s%s%s-{account_dv}' % tuple(account)
    # print(account_formatted)
    return account_formatted


print(f'Banco do Brasil\n{banco_do_brazil()}\n')
print(f'Santander\n{santander()}\n')
print(f'Caixa economica federal\n{caixa()}\n')
print(f'Itaú\n{itau()}\n')
print(f'Citibank\n{citibank()}\n')

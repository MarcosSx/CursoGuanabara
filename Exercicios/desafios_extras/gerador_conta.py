import math
from random import randint


def generic_agency_or_account(number_of_digits=4):
    account = list()
    for i in range(0, number_of_digits):
        account.append(randint(0, 9))
    return account


def generic_multiplier(multipliers):
    sum_numbers = 0
    for i, j in enumerate(reversed(multipliers), start=2):
        sum_numbers += i * j
    return sum_numbers


def formatter(list, type, digit=''):
    formatted = ''
    for i in list:
        formatted += str(i)
    if type.upper() in 'AG':
        return f'AG: {formatted} ' if str(digit) in '' else f'AG: {formatted}-{str(digit)} '
    elif type.upper() in 'CC':
        return f'CC: {formatted}-{str(digit)}'
    else:
        return f'AG: {formatted[:4]} CC: {formatted[4:]}-{digit}'


def banco_do_brazil():
    agency = generic_agency_or_account()
    account = generic_agency_or_account(8)

    sum_agency_dv = generic_multiplier(agency)
    sum_account_dv = generic_multiplier(account)

    agency_dv = abs((sum_agency_dv % 11) - 11)
    if agency_dv == 11 or agency_dv == 10:
        agency_dv = 0 if agency_dv == 10 else 'X'

    account_dv = abs((sum_account_dv % 11) - 11)
    if account_dv == 11 or account_dv == 10:
        account_dv = 0 if account_dv == 10 else 'X'

    agency_formatted = formatter(agency, 'A', agency_dv)
    account_formatted = formatter(account, 'CC', account_dv)
    return f'{agency_formatted}{account_formatted}'


def citibank():
    agency = generic_agency_or_account()
    account = generic_agency_or_account(7)

    sum_account_dv = generic_multiplier(account)

    account_dv = abs((sum_account_dv % 11) - 11)
    if account_dv == 11 or account_dv == 10:
        account_dv = 0

    agency_formatted = formatter(agency, 'AG')
    account_formatted = formatter(account, 'CC', str(account_dv))
    return f'{agency_formatted}{account_formatted}'


def itau():
    account = generic_agency_or_account(9)

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

    account_formatted = formatter(account, 'ALL', str(account_dv))
    return account_formatted


def caixa():
    agency = generic_agency_or_account()
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

    account_formatted = formatter(account, 'ALL', str(account_dv))
    return account_formatted


def santander():
    multipliers = [9, 7, 3, 1, 9, 7, 1, 3, 1, 9, 7, 3]
    agency = reversed(generic_agency_or_account())
    account = generic_agency_or_account(8)

    for i in agency:
        account.insert(0, i)

    sum_dv = 0
    for i in range(len(multipliers)):
        sum_dv += (multipliers[i] * account[i]) % 10

    account_dv = abs(sum_dv % 10 - 10)
    if sum_dv % 10 == 0:
        account_dv = 0

    account_formatted = formatter(account, 'ALL', str(account_dv))
    return account_formatted


def bradesco():
    agency = generic_agency_or_account()
    account = generic_agency_or_account(6)

    sum_agency_dv = generic_multiplier(agency)
    sum_account_dv = generic_multiplier(account)

    agency_dv = abs(sum_agency_dv % 11 - 11)
    if agency_dv == 10 or agency_dv == 11:
        agency_dv = 'P' if agency_dv == 10 else 0

    account_dv = abs(sum_account_dv % 11 - 11)
    if account_dv == 10 or account_dv == 11:
        account_dv = 'P' if account_dv == 10 else 0

    agency_formatted = formatter(agency, 'AG', agency_dv)
    account_formatted = formatter(account, 'CC', account_dv)
    return f'{agency_formatted}{account_formatted}'


def real():
    agency = generic_agency_or_account()
    account = generic_agency_or_account(7)
    multipliers = [8, 1, 4, 7, 2, 2, 5, 9, 3, 9, 5]

    for i in reversed(agency):
        account.insert(0, i)

    sum_account_dv = 0
    for i in range(len(multipliers)):
        sum_account_dv += account[i] * multipliers[i]

    account_dv = abs(sum_account_dv % 11 - 11)
    if sum_account_dv % 11 <= 1:
        account_dv = 1 if sum_account_dv == 0 else 1

    account_formatted = formatter(account, 'ALL', str(account_dv))
    return f'{account_formatted}'


def hsbc():
    agency = generic_agency_or_account()
    account = generic_agency_or_account(6)
    multipliers = [8, 9, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in reversed(agency):
        account.insert(0, i)

    sum_account_dv = 0
    for i in range(len(multipliers)):
        sum_account_dv += account[i] * multipliers[i]

    account_dv = abs(sum_account_dv % 11)
    if account_dv == 0 or account_dv == 10:
        account_dv = 0

    account_formatted = formatter(account, 'ALL', str(account_dv))
    return f'{account_formatted}'


print(f'Banco do Brasil\n{banco_do_brazil()}\n')
print(f'Santander\n{santander()}\n')
print(f'Bradesco\n{bradesco()}\n')
print(f'Caixa economica federal\n{caixa()}\n')
print(f'Itaú\n{itau()}\n')
print(f'Real\n{real()}\n')
print(f'Citibank\n{citibank()}\n')
print(f'HSBC\n{hsbc()}\n')

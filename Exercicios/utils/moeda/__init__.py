def metade(n, f=False):
    return f'R$ {n / 2:.2f}' if f else n / 2


def aumentar(n, porcentagem, f=False):
    return f'R$ {n + ((n * porcentagem) / 100):.2f}' if f else n + ((n * porcentagem) / 100)


def diminuir(n, porcentagem, f=False):
    return f'R$ {n - ((n * porcentagem) / 100):.2f}' if f else n - ((n * porcentagem) / 100)


def dobro(n, f=False):
    return f'R$ {n * 2:.2f}' if f else n * 2


def moeda(n):
    return f'R$ {n:.2f}'.replace('.', ',')


def resumo(p, aum, dim):
    print('-' * 35)
    print(f'{"RESOMO DO VALOR":^35}')
    print('-' * 35)
    print(f'{"Preço analizado:":<20} {moeda(p):<10}')
    print(f'{"Dobro do preço:":<20} {dobro(p, True):<10}')
    print(f'{"Metade do preço: ":<20} {metade(p, True):<10}')
    print(f'{str(aum) + "% de aumento:":<20} {aumentar(p, aum, True):<10}')
    print(f'{str(dim) + "% de redução:":<20} {diminuir(p, dim, True):<10}')
    print('-' * 35)


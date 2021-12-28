# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opcional) Mostara ou não a conta
    :return: O valor fatorial de um numero num.
    """
    f = 1
    linha = ''
    for c in range(num, 0, -1):
        f *= c
        linha += str(c)
        linha += ' = ' if linha[-1] == '1' else ' x '
    linha += str(f)
    return linha if show else f


print(fatorial(5, True))
help(fatorial)

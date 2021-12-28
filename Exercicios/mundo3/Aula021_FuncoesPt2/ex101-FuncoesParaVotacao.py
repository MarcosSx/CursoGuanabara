# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.

def voto(ano):
    """
    -> Calcula se o voto é ou não obrigatorio
    :param ano: O ano de Nascimento da pessoa
    :return: Obrigatoriedade ou não do voto
    """
    from datetime import date
    idade = date.today().year - ano
    return f'Com {idade} anos: VOTO OBRIGATÓRIO' if idade >= 18 else f'Com {idade} anos: VOTO NÃO OBRIGATORIO'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
help(voto)

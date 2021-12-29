# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

def notas(*notas, sit=False):
    """
    -> Função para analizar notas e situação de varios alunos
    :param notas: uma ou mais notas dos alunos (aceita varios)
    :param sit: (opcional), indicando se deve ou não adicionar a situação
    :return: dicionário com varias informações sobre a situação dos alunos
    """
    dados = {
        'total': len(notas),
        'maior': max(notas),
        'menor': min(notas),
        'média': sum(notas) / len(notas)
    }
    if sit:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['média'] <= 5:
            dados['situação'] = 'RUIM'
        else:
            dados['situação'] = 'RAZOAVEL'
    return dados


resp = notas(3, 8, 7)
notas(0, 6, 7, 6)
print(resp)

# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu
# aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista_expressao = list()
exp = str(input('Digite uma expressão: '))
for p in exp:
    if '(' in p:
        lista_expressao.append(p)
    elif ')' in p:
        if len(lista_expressao) > 0:
            lista_expressao.pop()
        else:
            lista_expressao.append(p)
            break
if len(lista_expressao) == 0:
    print('Expressao valida')
else:
    print('Expressão invalida')

# Adicione ao módolo moeda.py criado nos desafios anteriores, uma função resumo(), que mostre na tela algumas
# informações geradas pelas funções que ja temos no modulo criado até aqui.
from utils import moeda

p = float(input('Digite um preço: R$ '))
moeda.resumo(p, 80, 35)

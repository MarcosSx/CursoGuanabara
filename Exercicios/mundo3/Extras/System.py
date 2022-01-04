# Exercicio Python 115: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um
# arquivo de texto simples. O sitema só vai ter 3 opções: cadastrar uma nova pessoa, listar todas as pessoas cadastradas
# e sair do sistema.

from time import sleep
from lib.interface import *
from lib.arquivo import *

file = 'cursoemvideo.txt'
if not arquivoExiste(file):
    criarArquivo(file)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        # Opção de listar
        lerArquivo(file)
    elif resp == 2:
        # Opção de cadastrar novas pessoas.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(file, nome, idade)
    elif resp == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! digite uma opção valida.\033[m')
    sleep(0.3)

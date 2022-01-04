from mundo3.Extras.lib.interface import cabeçalho


def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('\033[31mHouve um ERRO ao ler o arquivo!\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for pos, l in enumerate(a):
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{pos + 1} - {dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um ERRO ao escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

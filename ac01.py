# Atividade Contínua 01
# Aluno 01: Lauro Mendes do Amaral Junior         RA: 1902047
# Aluno 02: Jeffersson Oliveira dos Santos        RA: 1901787
# Aluno 03: Verônica Bissi Gonçalves de Melo      RA: 1902220


def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        return alunos
    else:
        alunos[nome] = notas
        return alunos

    '''
    Essa função acrescenta os dados de um novo aluno no dicionário
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
        notas: lista com as notas de um aluno (valor)
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave já exista no dicionário,
        deve retornar o dicionário sem nenhuma alteração.
    '''


def remover_aluno(alunos, nome):
    if nome in alunos:
        alunos.pop(nome)
        return alunos
    else:
        return alunos

    '''
    Essa função exclui os dados de um aluno do dicionário.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave não exista no dicionário,
        deve retornar o dicionário sem nenhuma alteração.
    '''


def pesquisar_aluno(alunos, nome):
    if nome in alunos:
        a = alunos[nome]
        return a
    else:
        vazia = []
        return vazia

    '''
    Essa função deve retornar a lista com as notas de um aluno.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar uma lista com as notas do aluno
    Observação:
        Caso a chave não exista, deve retornar uma lista vazia
    '''


def calcular_media(alunos, nome):
    media_zero = 0
    if nome in alunos:
        a = sum(alunos[nome])
        media = a/5
        return media
    else:
        return media_zero
    '''
    Essa função retorna a média de um aluno.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar a média do aluno
    Observação:
        Caso a chave não exista, deve retornar zero
    '''


def calcular_media_turma(alunos):
    qtd_aluno = 0
    div_med = 0
    media_turma = 0
    for i in alunos:
        a = sum(alunos[i])
        media_turma = media_turma + a
        qtd_aluno = qtd_aluno + 1
    div_med = qtd_aluno * 5
    media_turma = media_turma / div_med
    return media_turma

    '''
    Essa função retorna a média geral da turma
    (soma de todas as notas dividida pela quantidade de todas as notas)
    Entrada:
        alunos: dicionario com os dados dos alunos
    Retorno:
        A função deve retornar a média geral da turma
    '''

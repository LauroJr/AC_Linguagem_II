import ac01

notas = []
alunos = {'pedro': [10, 9.5, 9, 5, 7],
          'ana': [4, 7, 9.5, 10, 8],
          'jose': [10, 4.5, 5, 6, 8]}

resposta = '999'
print("Escolha uma opção abaixo para prosseguir, ou digite 6 p/ sair: ")
print("[1] Adicionar Aluno")
print("[2] Remover Aluno")
print("[3] Pesquisar Aluno]")
print("[4] Calcular Média")
print("[5] Média da Turma")
while resposta != 6:
    resposta = int(input("Esolha uma opção acima: "))
    if resposta == 1:
        nome = input("Nome: ")
        for i in range(5):
            n = float(input("Nota: "))
            notas.append(n)
        a = ac01.adicionar_aluno(alunos, nome, notas)
        notas = []
        print(a)
    if resposta == 2:
        nome = input("Nome a ser removido: ")
        a = ac01.remover_aluno(alunos, nome)
        print(a)
    if resposta == 3:
        nome = input("Pesquise um aluno: ")
        a = ac01.pesquisar_aluno(alunos, nome)
        print(a)
    if resposta == 4:
        nome = input("Calcule a média de uma aluno Específico: ")
        a = ac01.calcular_media(alunos, nome)
        print(a)
    if resposta == 5:
        a = ac01.calcular_media_turma(alunos)
        print(a)

# TPC5: Aplicação para gestão de alunos
# aluno = [nome, id, [notaTPC, notaProj, notaTeste]]
# Turma: [aluno]

#..................................................................................
def criarTurma():
    nova_turma = []
    return nova_turma

#..................................................................................
def inserirAluno(turma, aluno):
    turma.append(aluno)
    print(f"Aluno {aluno[0]} inserido com sucesso!")
    return turma

#..................................................................................
def listarTurma(turma):
    print("- Listagem da Turma -")
    for aluno in turma:
        nome = aluno[0]
        num_id = aluno[1]
        notas = aluno[2]
        print(f"ID: {num_id} | Nome: {nome} | Notas: {notas}")
    return

#..................................................................................
def consultarAluno(turma, id_procurado):
    encontrado = False
    for aluno in turma:
        if str(aluno[1]) == str(id_procurado):
            print(f"Aluno encontrado: {aluno[0]} | Notas: {aluno[2]}")
            encontrado = True
    
    if not encontrado:
        print(f"Não foi encontrado nenhum aluno com o ID {id_procurado}.")
    return

#..................................................................................
def guardarTurma(turma, nome_ficheiro):
    f = open(nome_ficheiro, "w")
    for aluno in turma:
        linha = f"{aluno[0]};{aluno[1]};{aluno[2][0]};{aluno[2][1]};{aluno[2][2]}\n"
        f.write(linha)
    f.close()
    print(f"Turma guardada em '{nome_ficheiro}' com sucesso!")
    return

#..................................................................................
def carregarTurma(nome_ficheiro):
    nova_turma = []
    f = open(nome_ficheiro, "r")
    for linha in f:
        dados = linha.strip().split(";")
        nome = dados[0]
        num_id = dados[1]
        notas = [float(dados[2]), float(dados[3]), float(dados[4])]
        aluno = [nome, num_id, notas]
        nova_turma.append(aluno)
    f.close()
    print(f"Turma carregada de '{nome_ficheiro}' com sucesso!")
    return nova_turma

#..................................................................................
def menu():
    minha_turma = []
    continuar = True

    while continuar:
        print("""
        (1) Criar uma turma
        (2) Inserir um aluno na turma
        (3) Listar a turma
        (4) Consultar um aluno por id
        (8) Guardar a turma em ficheiro
        (9) Carregar uma turma dum ficheiro
        (0) Sair da aplicação
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            minha_turma = criarTurma()
            print("Turma nova (vazia) criada.")

        elif opcao == "2":
            nome = input("Nome do aluno: ")
            num_id = input("ID do aluno: ")
            n_tpc = float(input("Nota TPC: "))
            n_proj = float(input("Nota Projeto: "))
            n_teste = float(input("Nota Teste: "))
            novo_aluno = [nome, num_id, [n_tpc, n_proj, n_teste]]
            minha_turma = inserirAluno(minha_turma, novo_aluno)

        elif opcao == "3":
            listarTurma(minha_turma)

        elif opcao == "4":
            id_aluno = input("ID do aluno a procurar: ")
            consultarAluno(minha_turma, id_aluno)

        elif opcao == "8":
            nome_f = input("Nome do ficheiro para guardar (ex: turma.txt): ")
            guardarTurma(minha_turma, nome_f)

        elif opcao == "9":
            nome_f = input("Nome do ficheiro para carregar: ")
            minha_turma = carregarTurma(nome_f)

        elif opcao == "0":
            print("A sair... Bons estudos!")
            continuar = False
        
        else:
            print("Opção inválida!")

    return


menu()
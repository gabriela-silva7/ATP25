# TPC4: Aplicação para Gerir um Cinema
# Modelo: Sala = [nlugares, Vendidos, filme]
# Cinema = [Sala]

#..................................................................................
def inserirSala( cinema, sala ):
    existe = False
    for s in cinema:
        if s[2] == sala[2]:
            existe = True
            
    if not existe:
        cinema.append(sala)
        print(f"Sala do filme '{sala[2]}' inserida com sucesso!")
    else:
        print(f"Erro: Já existe uma sala a exibir o filme '{sala[2]}'.")
    
    return cinema

#..................................................................................
def listar( cinema ):
    print("\n--- Filmes em Exibição ---")
    for sala in cinema:
        print(f"Filme: {sala[2]}")
    return

#..................................................................................
def disponivel( cinema, filme, lugar ):
    for sala in cinema:
        if sala[2] == filme:
            if lugar <= sala[0] and lugar not in sala[1]:
                return True
            else:
                return False
    return False

#..................................................................................
def vendebilhete( cinema, filme, lugar ):
    if disponivel(cinema, filme, lugar):
        for sala in cinema:
            if sala[2] == filme:
                sala[1].append(lugar)
                print(f"Bilhete para o lugar {lugar} (Filme: {filme}) vendido!")
    else:
        print(f"O lugar {lugar} não está disponível para o filme {filme}!")
    
    return cinema

#..................................................................................
def listardisponibilidades( cinema ):
    print("\n--- Disponibilidades por Sala ---")
    for sala in cinema:
        filme = sala[2]
        total_lugares = sala[0]
        ocupados = len(sala[1])
        disponiveis = total_lugares - ocupados
        print(f"Filme: {filme} | Lugares Disponíveis: {disponiveis}")
    return

#..................................................................................
def consultarSala( cinema, filme ):
    for sala in cinema:
        if sala[2] == filme:
            print(f"Filme: {sala[2]} | Lotação: {sala[0]} | Lugares Ocupados: {sala[1]}")
    return

#..................................................................................
def menu():
    meu_cinema = []
    continuar = True

    while continuar:
        print("""
        (1) Inserir Nova Sala
        (2) Listar Filmes
        (3) Consultar Disponibilidade de Lugar
        (4) Vender Bilhete
        (5) Listar Disponibilidades Totais
        (6) Consultar Sala (Detalhes)
        (0) Sair
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            filme = input("Nome do filme: ")
            lotacao = int(input("Lotação da sala: "))
            nova_sala = [lotacao, [], filme]
            meu_cinema = inserirSala(meu_cinema, nova_sala)

        elif opcao == "2":
            listar(meu_cinema)

        elif opcao == "3":
            filme = input("Nome do filme: ")
            lugar = int(input("Número do lugar: "))
            if disponivel(meu_cinema, filme, lugar):
                print(f"O lugar {lugar} está livre!")
            else:
                print(f"O lugar {lugar} está ocupado ou nao existe.")

        elif opcao == "4":
            filme = input("Nome do filme: ")
            lugar = int(input("Número do lugar: "))
            meu_cinema = vendebilhete(meu_cinema, filme, lugar)

        elif opcao == "5":
            listardisponibilidades(meu_cinema)

        elif opcao == "6":
            filme = input("Qual o filme que quer consultar? ")
            consultarSala(meu_cinema, filme)

        elif opcao == "0":
            print("A fechar o sistema de gestão... Até logo!")
            continuar = False
        
        else:
            print("Opção inválida!")

    return meu_cinema

menu()
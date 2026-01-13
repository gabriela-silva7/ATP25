# Relatório do TPC 4
## Maria Gabriela Silva a107194


Neste tpc, segui a sugestão do enunciado e usei os índices da lista para aceder à informação.
Criei a função inserirSala que, antes de adicionar uma nova sala ao cinema, verifica se já existe algum filme com o mesmo nome para evitar duplicados.

Para a gestão de bilhetes fiz uma função disponivel que verifica duas coisas: se o número do lugar existe naquela sala e se ele ainda não está na lista de vendidos.
A função vendebilhete utiliza a função anterior, se o lugar estiver livre, ela faz um append do número do lugar à lista de ocupados daquela sala.

Criei a função listar para mostrar apenas os nomes dos filmes em exibição.
Fiz a função listardisponibilidades que percorre todas as salas e faz a conta: lotação total, quantidade de bilhetes vendidos, mostrando o resultado para cada filme.

Fiz um menu com um ciclo while e uma variável de controlo (continuar). O utilizador pode escolher as opções de 1 a 6 para gerir o cinema ou 0 para sair do programa.
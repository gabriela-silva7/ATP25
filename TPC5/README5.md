# Relatório TPC5
## Maria Gabriela Silva a107194

Estruturei o aluno como [nome, id, [nota1, nota2, nota3]]. Para aceder às notas, usei índices duplos (por exemplo, aluno[2][0] para chegar à primeira nota).

Gestão da Turma:
* Criei a função inserirAluno que recebe os dados do utilizador e faz o append do novo aluno à lista da turma.
* Fiz uma função que percorre a turma e compara o ID introduzido com o aluno[1]. Se encontrar, mostra os dados, se não, avisa que o aluno não existe.

Ficheiros:

* Usei a função open com o modo "w". Para cada aluno, escrevo uma linha no ficheiro onde separo o nome, o ID e as três notas por pontos e vírgulas.

* Usei o modo "r" para ler o ficheiro. Uso o split(";") para separar a linha de volta nos dados originais e volto a montar a lista do aluno para a carregar na memória do programa. Tive de transformar os IDs em strings na hora de comparar, para não haver erros caso o utilizador escreva números ou letras. Na leitura do ficheiro, usei o float() para garantir que as notas voltam a ser números decimais e não apenas texto.

O menu tem as opções pedidas (1, 2, 3, 4, 8, 9 e 0). Usei o sistema de if/elif dentro de um ciclo while com a variável continuar, para que o utilizador possa fazer várias operações seguidas sem o programa fechar.


## TPC3

import random

def criar_lista_aleatoria():
    nova_lista = []
    tamanho = int(input("Quantos números queres na lista? "))
    i = 0
    while i < tamanho:
        nova_lista.append(random.randint(1, 100))
        i = i + 1
    return nova_lista

def ler_lista_utilizador():
    nova_lista = []
    tamanho = int(input("Quantos números vais introduzir? "))
    i = 0
    while i < tamanho:
        num = int(input(f"Introduz o número {i+1}: "))
        nova_lista.append(num)
        i = i + 1
    return nova_lista

def calcular_soma(l):
    total = 0
    for x in l:
        total = total + x
    return total

def calcular_maior(l):
    maior = l[0]
    for x in l:
        if x > maior:
            maior = x
    return maior

def calcular_menor(l):
    menor = l[0]
    for x in l:
        if x < menor:
            menor = x
    return menor

def verificar_crescente(l):
    ordenada = "Sim"
    i = 0
    while i < len(l) - 1:
        if l[i] > l[i+1]:
            ordenada = "Não"
        i = i + 1
    return ordenada

def verificar_decrescente(l):
    ordenada = "Sim"
    i = 0
    while i < len(l) - 1:
        if l[i] < l[i+1]:
            ordenada = "Não"
        i = i + 1
    return ordenada

def procurar_elemento(l, alvo):
    posicao = -1
    i = 0
    while i < len(l):
        if l[i] == alvo:
            if posicao == -1:
                posicao = i
        i = i + 1
    return posicao

lista_interna = []
opcao = -1

while opcao != 0:
    print("\n--- MENU ---")
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) estaOrdenada por ordem crescente")
    print("(8) estaOrdenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")
    
    opcao = int(input("Escolhe uma opção: "))
    
    if opcao == 1:
        lista_interna = criar_lista_aleatoria()
        print("Lista criada:", lista_interna)
        
    elif opcao == 2:
        lista_interna = ler_lista_utilizador()
        print("Lista guardada:", lista_interna)
        
    elif opcao == 3:
        if len(lista_interna) > 0:
            resultado = calcular_soma(lista_interna)
            print("Soma:", resultado)
        else:
            print("A lista está vazia!")
            
    elif opcao == 4:
        if len(lista_interna) > 0:
            soma = calcular_soma(lista_interna)
            media = soma / len(lista_interna)
            print("Média:", media)
        else:
            print("A lista está vazia!")
            
    elif opcao == 5:
        if len(lista_interna) > 0:
            print("Maior:", calcular_maior(lista_interna))
        else:
            print("A lista está vazia!")
            
    elif opcao == 6:
        if len(lista_interna) > 0:
            print("Menor:", calcular_menor(lista_interna))
        else:
            print("A lista está vazia!")
            
    elif opcao == 7:
        if len(lista_interna) > 0:
            print("Está ordenada de forma crescente?", verificar_crescente(lista_interna))
        else:
            print("A lista está vazia!")
            
    elif opcao == 8:
        if len(lista_interna) > 0:
            print("Está ordenada de forma decrescente?", verificar_decrescente(lista_interna))
        else:
            print("A lista está vazia!")
            
    elif opcao == 9:
        if len(lista_interna) > 0:
            valor = int(input("Que número procuras? "))
            print("Posição do elemento:", procurar_elemento(lista_interna, valor))
        else:
            print("A lista está vazia!")
            
    elif opcao == 0:
        print("A sair... Lista final:", lista_interna)
    
    else:
        if opcao != 0:
            print("Opção inválida!")
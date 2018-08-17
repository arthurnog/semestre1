#!/usr/bin/env python3
#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
    a = jogo.split(' ')
    for i in range(len(tabela)):
        if a[0] == tabela[i][0]:
            if int(a[1]) > int(a[3]):
                tabela[i][1] += 3#para cada vitoria 3 é somado ao numero de pontos
                tabela[i][2] += 1#1 é somado ao numero de vitorias
            if int(a[1]) == int(a[3]):
                tabela[i][1] += 1
            tabela[i][3] += (int(a[1])-int(a[3]))#aqui é atualizado o saldo de gols
            tabela[i][4] += int(a[1])#aqui é atualido o gols pro
        if a[4] == tabela[i][0]:
            if int(a[3]) > int(a[1]):
                tabela[i][1] += 3#para cada vitoria 3 é somado ao numero de pontos
                tabela[i][2] += 1#1 é somado ao numero de vitorias
            if int(a[1]) == int(a[3]):
                tabela[i][1] += 1
            tabela[i][3] += (int(a[3])-int(a[1]))#aqui é atualizado o saldo de gols
            tabela[i][4] += int(a[3])#aqui é atualido o gols pro
    return tabela
#*******************************************************************************

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
    if time1 > time2:
        return 1
    if time1 < time2:
        return -1
    if time1 == time2:
        return 0
#*******************************************************************************

#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
    for i in range(1, len(tabela)):
        aux = tabela[i]
        j = i - 1
        while (j>=0):
            if tabela[j][1]<aux[1]:
                tabela[j+1] = tabela[j]
                j = j - 1
            elif tabela[j][1] == aux[1] and tabela[j][2]<aux[2]:
                tabela[j+1] = tabela[j]
                j = j - 1
            elif tabela[j][1] == aux[1] and tabela[j][2] == aux[2] and tabela[j][3]<aux[3]:
                tabela[j+1] = tabela[j]
                j = j - 1
            elif tabela[j][1] == aux[1] and tabela[j][2] == aux[2] and tabela[j][3] == aux[3] and tabela[j][4]<aux[4]:
                tabela[j+1] = tabela[j]
                j = j - 1
        tabela[j+1] = aux
    return tabela
#*******************************************************************************


#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
    for i in range(len(tabela)):
        for j in range(len(tabela[0])):
            tabela[i][j] = str(tabela[i][j])
        sep = ', '
        lis = sep.join(tabela[i])
        print(lis)
    return None
#*******************************************************************************

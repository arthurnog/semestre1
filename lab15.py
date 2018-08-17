#!/usr/bin/env python3

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    if num in conj:
        return True
    else:
        return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    cont = 0
    for i in range(len(conj1)):
        if conj1[i] in conj2:
            cont += 1
    if cont == len(conj1):
        return True
    else:
        return False

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    if num not in conj:
        conj.append(num)
        for i in range(1, len(conj)):
          aux = conj[i]
          j=i-1
          while(j>=0 and conj[j] > aux):
            conj[j+1] = conj[j]
            j = j-1
          conj[j+1] = aux
    return conj

def subtracao(conj, num):
    if num in conj:
        a = conj.index(num)
        del conj[a]
    return conj

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    conj3 = []
    for i in range(len(conj1)):
        conj3.append(conj1[i])
    for i in range(len(conj2)):
        if conj2[i] not in conj1:
            conj3.append(conj2[i])
    for i in range(1, len(conj3)):
      aux = conj3[i]
      j=i-1
      while(j>=0 and conj3[j] > aux):
        conj3[j+1] = conj3[j]
        j = j-1
      conj3[j+1] = aux
    return conj3

def intersecao(conj1, conj2):
    conj3 = []
    for i in range(len(conj2)):
        if conj2[i] in conj1:
            conj3.append(conj2[i])
    for i in range(1, len(conj3)):
      aux = conj3[i]
      j=i-1
      while(j>=0 and conj3[j] > aux):
        conj3[j+1] = conj3[j]
        j = j-1
      conj3[j+1] = aux
    return conj3

def diferenca(conj1, conj2):
    #conj1 - conj2
    conj3 = []
    for i in range(len(conj1)):
        if conj1[i] not in conj2:
            conj3.append(conj1[i])
    for i in range(1, len(conj3)):
      aux = conj3[i]
      j=i-1
      while(j>=0 and conj3[j] > aux):
        conj3[j+1] = conj3[j]
        j = j-1
      conj3[j+1] = aux
    return conj3

def uniao_disjunta(conj1, conj2):
    conj3 = []
    for i in range(len(conj1)):
        if conj1[i] not in conj2:
            conj3.append(conj1[i])
    for j in range(len(conj2)):
        if conj2[j] not in conj1:
            conj3.append(conj2[j])
    for i in range(1, len(conj3)):
      aux = conj3[i]
      j=i-1
      while(j>=0 and conj3[j] > aux):
        conj3[j+1] = conj3[j]
        j = j-1
      conj3[j+1] = aux
    return conj3

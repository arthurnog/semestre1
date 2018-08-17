#!/usr/bin/env python3

# Laboratorio 12 - Tetris
# Nome:Arthur Lucas da Silva Nogueira
# RA:213293

ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10

# Funcao: atualiza_posicao
#
# Parametros:
#      l: largura do bloco que ira cair
#      a: altura do bloco que ira cair
#      x: posicao horizontal inicial do bloco que ira cair
#   desl: deslocamento horizontal a ser aplicado ao bloco (positivo para direita, negativo para a esquerda)
#    rot: 1 se deve rotacionar o bloco, 0 caso contrario
#
# Retorno:
#   Nova largura, altura e posicao horizontal.
#
def atualiza_posicao(l, a, x, desl, rot):
    a1 = a
    l1 = l
    if rot == 1:
        a = l1
        l = a1
    if rot == 0:
        a = a1
        l = l1
    x = x + desl
    if x < 0:
        x = 0
    if x > 10 - l:
        x = 10 - l
    return l, a, x

# Funcao: encontra_y
#
# Parametros:
#    matriz: matriz representando o tabuleiro
#      l: largura do bloco que ira cair
#      x: posicao horizontal do bloco que ira cair
#
# Retorno:
#   altura final y do canto inferior esquerdo do bloco apos
#   este descer o maximo possivel
#
def encontra_y(matriz, l, x):
    y = 0
    for j in range(10):
        for i in range(x, x+l):
            if matriz[j][i] == 1:
                y = j + 1
    return y

# Funcoes: posicao_final_valida
#
# Parametros:
#      a: altura do bloco que caiu
#      y: altura final do bloco que caiu
#
# Retorno:
#   1 se o bloco naquela posicao estiver contido dentro do tabuleiro, ou 0 caso contrario.
#
def posicao_final_valida(a, y):
    if a > 10 - y:
        return 0
    else:
        return 1
# Funcoes: posiciona_bloco
#
# Parametros:
#    matriz: matriz do tabuleiro
#      l: largura do novo bloco
#      a: altura do novo bloco
#      x: posicao horizontal do novo bloco
#      y: altura final do novo bloco
#
#      Deve preencher com 1s as novas posicoes ocupadas pelo bloco que caiu
# Retorno:
#   NULL
#
def posiciona_bloco(matriz, l, a, x, y):
    if x + l >= 10:
        x = 10 - l
    for i in range(x, x+l):
        if y+a <= 10:
            for j in range(y, y+a):
                matriz[j][i] = 1
        else:
            for j in range(y, 10):
                matriz[j][i] = 1
    return None
# Funcoes: atualiza_matriz
#
#    matriz: matriz do tabuleiro
#
#         Deve remover as linhas totalmente preenchidas do tabuleiro copiando
#         linhas posicionadas acima.
# Retorno:
#   retorna o numero de linhas totalmente preenchidas que foram removidas apos
#   a atualizacao do tabuleiro.
#
def atualiza_matriz(matriz):
    m = 0
    i = 0
    while i < 10:
        if matriz[i] == ([1]*10) and i != 10:
            del matriz[i]
            matriz.append(([0]*10))
            m = m + 1
            i -= 1
        i += 1
    return m

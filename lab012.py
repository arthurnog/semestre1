tabuleiro = []
ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10
for i in range(ALTURA_TABULEIRO):
    l = []
    for j in range(LARGURA_TABULEIRO):
        l.append(0)
    tabuleiro.append(l)
n = int(input())#numero de blocos que vão cair
contador = 1
matparametros = []#matriz que contem os parametros atualizados dos blocos

def atualiza_posicao(l, a, x, desl, rot):#essa função desloca e rotaciona o bloco que ira cair no tabuleiro
    desl = parametros[3]
    rot = parametros[4]
    x = x + desl
    if rot == 1:
        l = parametros[1]
        a = parametros[0]
    elif rot == 0:
        l = parametros[0]
        a = parametros[1]
    return l, a, x

while contador <= n:
    linha = input()
    parametros = [int(i) for i in linha.split()]#lista com os parametros analisados
    l = parametros[0]
    a = parametros[1]
    x = parametros[2]
    atualiza_posicao(parametros)
    matparametros.append(parametros)
    contador += 1
print(matparametros)
print(parametros)

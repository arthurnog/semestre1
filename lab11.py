# Nome:Arthur Lucas da Silva Nogueira
# RA:213293
LeC = input()#numero de linhas e colunas
dados = [int(i) for i in LeC.split()]
linhas = dados[0]
colunas = dados[1]
dias = int(input())
matriz = []
matriz2 = []
for i in range(linhas):
    HZouC = input()#humanos, zumbies ou casas vazias
    casas = [int(i) for i in HZouC.split()]
    casas.append(0)
    casas.insert(0, 0)
    matriz.append(casas)
    matriz2.append(casas)
matriz.append([0]*(colunas +2))
matriz.insert(0, [0]*(colunas +2))
matriz2.append([0]*(colunas +2))
matriz2.insert(0, [0]*(colunas +2))
for k in range(dias+1):
    print("iteracao", k)
    if k == 0:
        for i in range(1, linhas + 1):
            for j in range(1, colunas + 1):
                print(matriz[i][j], end = "")
            print("")
    else:
        for i in range(1, linhas + 1):
            matriz[i]=matriz2[i][:]
            for j in range(1, colunas + 1):
                h = 0
                if matriz[i][j] == 0:
                    if matriz[i-1][j] == 1:
                        h += 1
                    if matriz[i+1][j] == 1:
                        h += 1
                    if matriz[i][j+1] == 1:
                        h += 1
                    if matriz[i][j-1] == 1:
                        h += 1
                    if matriz[i-1][j-1] == 1:
                        h += 1
                    if matriz[i-1][j+1] == 1:
                        h += 1
                    if matriz[i+1][j-1] == 1:
                        h += 1
                    if matriz[i+1][j+1] == 1:
                        h += 1
                    if h == 2:
                        matriz2[i][j] = 1
                if matriz[i][j] == 1:
                    if matriz[i-1][j] == 2 or matriz[i+1][j] == 2 or matriz[i-1][j+1] == 2 or matriz[i-1][j-1] == 2 or matriz[i+1][j+1] == 2 or matriz[i+1][j-1] == 2 or matriz[i][j+1] == 2 or matriz[i][j-1] == 2:
                        matriz2[i][j] = 2
                if matriz[i][j] == 2:
                    if matriz[i-1][j] == 1:
                        h += 1
                    if matriz[i+1][j] == 1:
                        h += 1
                    if matriz[i][j+1] == 1:
                        h += 1
                    if matriz[i][j-1] == 1:
                        h += 1
                    if matriz[i-1][j-1] == 1:
                        h += 1
                    if matriz[i-1][j+1] == 1:
                        h += 1
                    if matriz[i+1][j-1] == 1:
                        h += 1
                    if matriz[i+1][j+1] == 1:
                        h += 1
                    if h != 1:
                        matriz2[i][j] = 0
        matriz = matriz2[:]
        for i in range(1, linhas + 1):
            for j in range(1, colunas + 1):
                print(matriz[i][j], end = "")
            print("")

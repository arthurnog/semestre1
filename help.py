d = int(input())#numero de dias analisados
precos = []#matriz de preços de ações de cada empresa
matlucro = [[],[],[],[]]#matriz com os possíveis lucros das compras e vendas de cada empresa
matLucroT = []

for i in range (d):
    row = []
    for i in range(4):
        row.append(0)
    matLucroT.append(row)

for i in range (4):
    for j in range(d):
        matLucroT[j][i] = matLucro[i][j]

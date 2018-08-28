#Arthur Lucas da Silva Nogueira 213293
d = int(input())#numero de dias analisados
precos = []#matriz de preços de ações de cada empresa
matlucro = [[],[],[],[]]#matriz com os possíveis lucros das compras e vendas de cada empresa
matLucroT = []
lucro_total = 0
dia_compra = 0
dia_venda = 0
lucro = 0
for i in range (4):
    row = []
    for i in range(d):
        row.append(float(input()))
    precos.append(row)
for i in range (d):
    row = []
    for i in range(4):
        row.append(0)
    matLucroT.append(row)
for i in range(d):#aqui eu armazeno os possiveis lucros entre os dias de compra e venda da empresa 1
    c1 = precos[0][i]#valor de compra da empresa 1
    for j in range(d):
        v1 = precos[0][j]#valor de venda da empresa 1
        if precos[0].index(v1) > precos[0].index(c1):
            l = v1 - c1#calculo do lucro é feito apenas se a venda for feita em algum dia após a compra
            matlucro[0].append(l)
for i in range(d):#aqui eu armazeno os possiveis lucros entre os dias de compra e venda da empresa 2
    c2 = precos[1][i]#valor de compra
    for j in range(d):
        v2 = precos[1][j]#valor de venda
        if precos[1].index(v2) > precos[1].index(c2):
            l = v2 - c2#calculo do lucro é feito apenas se a venda for feita em algum dia após a compra
            matlucro[1].append(l)
for i in range(d):#aqui eu armazeno os possiveis lucros entre os dias de compra e venda da empresa 3
    c3 = precos[2][i]#valor de compra
    for j in range(d):
        v3 = precos[2][j]#valor de venda
        if precos[2].index(v3) > precos[2].index(c3):
            l = v3 - c3#calculo do lucro é feito apenas se a venda for feita em algum dia após a compra
            matlucro[2].append(l)
for i in range(d):#aqui eu armazeno os possiveis lucros entre os dias de compra e venda da empresa 4
    c4 = precos[3][i]#valor de compra
    for j in range(d):
        v4 = precos[3][j]#valor de venda
        if precos[3].index(v4) > precos[3].index(c4):
            l = v4 - c4#calculo do lucro é feito apenas se a venda for feita em algum dia após a compra
            matlucro[3].append(l)
for i in range (4):
    for j in range(d):
        matLucroT[j][i] = matlucro[i][j]
for j in range(d):
    lucro_total += max(matLucroT[j])

print(precos)
print(matlucro)
print(matLucroT)
print(lucro_total)

#print("acao %d: compra %d, venda %d, lucro %.2f" % (empresa, dia_compra, dia_venda, lucro))
#print("Lucro: %.2f" % (lucro_total))

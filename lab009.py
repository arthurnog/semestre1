#Arthur Lucas da Silva Nogueira 213293
#se der certo MUDA O NOME DO LAB
lucro_total = 0
acao = 0
lucro = 0
dia_compra = 0
dia_venda = 0
precos = []
dias_totais = int(input())
for i in range (4):
    row = []
    for i in range(d):
        row.append(float(input()))
    precos.append(row)
for i in range(dias_totais):
    for j in range(dias_totais):
        for k in range(dias_totais):
            for l in range(dias_totais):
                for m in range(dias_totais):
                    for n in range(dias_totais):
                        for o in range(dias_totais):
                            for p in range(dias_totais):
                                c1 = precos[0][i]#valor de compra da empresa 1
                                v1 = precos[0][j]#valor de venda da empresa 1
                                l1 = v1 - c1#calculo do lucro é feito apenas se a venda for feita em algum dia após a compra
                                c2 = precos[1][k]#valor de compra da empresa 2
                                v2 = precos[1][l]#valor de venda da empresa 2
                                l2 = v2 - c2#calculo do lucro é feito apenas se a venda for feita em algum dia após a compra
                                c3 = precos[2][m]#valor de compra da empresa 3
                                v3 = precos[2][n]#valor de venda da empresa 3
                                l3 = v3 - c3#calculo do lucro é feito apenas se a venda for feita em algum dia após a compra
                                c4 = precos[3][o]#valor de compra da empresa 4
                                v4 = precos[3][p]#valor de venda da empresa 4
                                l4 = v4 - c4#calculo do lucro é feito apenas se a venda for feita em algum dia após a compra




#print("acao %d: compra %d, venda %d, lucro %.2f" % (empresa, dia_compra, dia_venda, lucro))
#print("Lucro: %.2f" % (lucro_total))

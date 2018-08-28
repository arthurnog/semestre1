#Arthur Lucas da Silva Nogueira 213293
#NÃO ESQUECE DE MUDAR O NOME DO LAB PELO AMOR DE DEUS
d = int(input())#numero de dias
E1 = []#valores da empresa 1
E2 = []#valores da empresa 2
E3 = []#valores da empresa 3
E4 = []#valores da empresa 4
lucro1 = []#possiveis lucros das vendas de acoes da empresa 1
lucro2 = []#possiveis lucros das vendas de acoes da empresa 2
lucro3 = []#possiveis lucros das vendas de acoes da empresa 3
lucro4 = []#possiveis lucros das vendas de acoes da empresa 4
lucro = 0
lucro_total = 0#soma dos lucros gerados pelas vendas das empresas
empresa = 0
dia_venda = 0
dia_compra = 0
for i in range(d):#eu adiciono os valores das empresas em cada uma das listas
    e = float(input())
    E1.append(e)
for i in range(d):
    e = float(input())
    E2.append(e)
for i in range(d):
    e = float(input())
    E3.append(e)
for i in range(d):
    e = float(input())
    E4.append(e)
for i in range(d):#aqui eu armazeno os possiveis lucros entre os dias de compra e venda da empresa 1
    c1 = E1[i]#valor de compra
    for j in range(d):
        v1 = E1[j]#valor de venda
        if E1.index(v1) > E1.index(c1):
            l = v1 - c1#calculo do lucro é feito apenas se a venda for feita em algum dia após a compra
            lucro1.append(l)
for i in range(d):#aqui eu armazeno os possiveis lucros entre os dias de compra e venda da empresa 2
    c2 = E2[i]
    for j in range(d):
        v2 = E2[j]
        if E2.index(v2) > E2.index(c2):
            l = v2 - c2
            lucro2.append(l)
for i in range(d):#aqui eu armazeno os possiveis lucros entre os dias de compra e venda da empresa 3
    c3 = E3[i]
    for j in range(d):
        v3 = E3[j]
        if E3.index(v3) > E3.index(c3):
            l = v3 - c3
            lucro3.append(l)
for i in range(d):#aqui eu armazeno os possiveis lucros entre os dias de compra e venda da empresa 4
    c4 = E4[i]
    for j in range(d):
        v4 = E4[j]
        if E4.index(v4) > E4.index(c4):
            l = v4 - c4
            lucro4.append(l)
maiorlucro1 = max(lucro1)
maiorlucro2 = max(lucro2)
maiorlucro3 = max(lucro3)
maiorlucro4 = max(lucro4)
if maiorlucro1 > 0:
    lucro_total += maiorlucro1
if maiorlucro2 > 0:
    lucro_total += maiorlucro2
if maiorlucro3 > 0:
    lucro_total += maiorlucro3
if maiorlucro4 > 0:
    lucro_total += maiorlucro4

print(lucro1)
print(lucro2)
print(lucro3)
print(lucro4)
print(lucro_total)


#print("acao %d: compra %d, venda %d, lucro %.2f" % (empresa, dia_compra, dia_venda, lucro))
#print("Lucro: %.2f" % (lucro_total))

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
for i in range(len(E1)):#aqui eu avalio os possiveis lucros entre os dias de compra e venda da empresa 1
    c1 = E1[i]
    for j in range(len(E1)):
        v1 = E1[j]
        lucro = v1 - c1
        if lucro > 0:
            lucro1.append(lucro)
for i in range(len(E1)):#aqui eu avalio os possiveis lucros entre os dias de compra e venda da empresa 2
    c2 = E2[i]
    for j in range(len(E1)):
        v2 = E2[j]
        lucro = v2 - c2
        if lucro > 0:
            lucro2.append(lucro)
for i in range(len(E3)):#aqui eu avalio os possiveis lucros entre os dias de compra e venda da empresa 3
    c3 = E3[i]
    for j in range(len(E3)):
        v3 = E3[j]
        lucro = v3 - c3
        if lucro > 0:
            lucro3.append(lucro)
for i in range(len(E4)):#aqui eu avalio os possiveis lucros entre os dias de compra e venda da empresa 4
    c4 = E4[i]
    for j in range(len(E4)):
        v4 = E4[j]
        lucro = v4 - c4
        if lucro > 0:
            lucro4.append(lucro)
print(lucro1)
print(lucro2)
print(lucro3)
print(lucro4)

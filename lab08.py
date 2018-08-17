#Arthur Lucas da Silva Nogueira 213293
import math
N = int(input())#numero de monstros observados
lstId = []#lista de identificadores
lstMd = []#lista de multiplicadores de poder dos monstros
for k in range(N):#criando listas de indentificadores e multiplicadores
    linha = input()#entradas
    ints = [int(i) for i in linha.split()]#lista que acumula as entradas
    I = ints[0]#identificador do monstro
    PCa = ints[1]#poder de combate atual do monstro
    PCf = ints[2]#poder de combate futuro do monstro
    mult = (PCf / PCa)#fator multiplicador obtido na evolucao
    lstId.append(I)#adiciona um identificador a lista de identificadores
    lstMd.append(mult)#adiciona um multiplicador a lista de multiplicadores
linha = input()#entradas
ints = [int(i) for i in linha.split()]
while linha != "0 0":
    termos=0 #número de monstros com o mesmo identificador
    somaMultiplicadores=0#soma dos multiplicadores dos monstros de mesmo Identificador
    for j in range(len(lstId)):
        if ints[0] == lstId[j]:
            somaMultiplicadores+=lstMd[j]
            termos+=1
    PCa = ints[1]
    if termos!=0:
        multiplicadorgeral=somaMultiplicadores/termos
        print(math.ceil(PCa*multiplicadorgeral))
        somaMultiplicadores=0
        termos=0
        multiplicadorgeral=0
    linha = input()#entradas
    ints = [int(i) for i in linha.split()]

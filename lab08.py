#Arthur Lucas da Silva Nogueira 213293
import math
N = int(input())#numero de monstros observados
linha = input()#dados dos monstros
ints = [int(i) for i in linha.split()]#os dados são acumulados nessa lista
while len(ints) == 3:
    I = ints[0]#identificador do monstro
    PCa = ints[1]#poder de combate atual do monstro
    PCf = ints[2]#poder de combate futuro do monstro
    mult = math.ceil(PCf / PCa)#fator multiplicador obtido na evolucao
    linha = input()
    ints = [int(i) for i in linha.split()]

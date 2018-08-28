#Arthur Lucas da Silva Nogueira 213293
#este programa e um simulador de luta entre dois personagens, ken e ryu, cada um tem 50 pontos de vida e o jogo acaba depois de dois rounds, com a vitoria de um ou com um empate
#ao digitar um valor (punch) e ele for positivo ele sera acumulado na variavel pos se for negativo e acumulado em neg
#quando a vida cai pra zero o contado de rounds (rt) e diminuido de um, quando ele cai pra 0 a luta acaba
#se ror, que e o numero de rounds vencido pelo ryu, for igual a dois ryu ganha, se rok for dois ken ganha
#se ror e rok forem iguais a 1 a disputa acaba em empate
#diferente do programa anterior ha multiplicadores de dano, caso o numero seja triangular ou perfeito
ror = 0
rok = 0
ken = 2000
ryu = 2000
pos = 0
neg = 0
rt = 2
lst = []
a = 0
for i in range(1,1000):#aqui eu crio uma lista de numeros triangulares para ser comparado com o numero que sera digitado
    a += i
    lst.append(a)
while rt != 0:
    soma = 0
    cont = 1
    punch = int(input())
    if punch > 0:
        while cont < punch:#aqui eu verifico se o numero é perfeito
            if punch%cont == 0:
                soma = soma + cont
                cont = cont + 1
            else:
                cont = cont + 1
        if soma == punch and punch in lst:#se o numero e perfeito e pertence a lista de valores triangulares o dano e multiplicado por 3
            punch = punch * 3
        elif soma == punch:#se o numero e perfeito o dano e multiplicado por 3
            punch = punch * 3
        elif punch in lst:#se o numero e triangular o dano e multiplicado por 2
            punch = punch * 2
        pos = pos + punch
        if ken > 0:
            if neg < 0:
                print("Ryu: %d" %ryu + " - %d" %(-1 * neg) + " = %d" %(ryu + neg))
                ryu = ryu + neg
                neg = 0
        if pos >= ken:
            print("Ken: %d" %ken + " - %d" %pos + " = %d" %(ken - pos))
            ror = ror + 1
            rt = rt - 1
            ken = 2000
            ryu = 2000
            pos = 0
    elif punch < 0:
        while cont < (-1 * punch):
            if (-1 * punch)%cont == 0:
                soma = soma + cont
                cont = cont + 1
            else:
                cont = cont + 1
        if soma == (-1 * punch) and (-1 * punch) in lst:
            punch = punch * 3
        elif soma == (-1 * punch):
            punch = punch * 3
        elif (-1 * punch) in lst:
            punch = punch * 2
        neg = neg + punch
        if ryu > 0:
            if pos > 0:
                print("Ken: %d" %ken + " - %d" %pos + " = %d" %(ken - pos))
                ken = ken - pos
                pos = 0
        if neg <= (-1*ryu):
            print("Ryu: %d" %ryu + " - %d" %(-1 * neg) + " = %d" %(ryu + neg))
            rok = rok + 1
            rt = rt - 1
            ryu = 2000
            ken = 2000
            neg = 0
if ror == 2:
	print("Ryu venceu")
elif rok == 2:
	print("Ken venceu")
elif ror == 1 and rok == 1:
	print("empatou")

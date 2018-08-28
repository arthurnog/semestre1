#Arthur Lucas da Silva Nogueira 213293
#este programa e um simulador de luta entre dois personagens, ken e ryu, cada um tem 50 pontos de vida e o jogo acaba depois de dois rounds, com a vitoria de um ou com um empate
#ao digitar um valor (punch) e ele for positivo ele sera acumulado na variavel pos se for negativo e acumulado em neg
#quando a vida cai pra zero o contado de rounds (rt) e diminuido de um, quando ele cai pra 0 a luta acaba
#se ror, que e o numero de rounds vencido pelo ryu, for igual a dois ryu ganha, se rok for dois ken ganha
#se ror e rok forem iguais a 1 a disputa acaba em empate
ror = 0
rok = 0
ken = 50
ryu = 50
pos = 0
neg = 0
rt = 2
while rt != 0:
	punch = int(input())
	if punch > 0:
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
			ken = 50
			ryu = 50
			pos = 0
	elif punch < 0:
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
			ryu = 50
			ken = 50
			neg = 0
if ror == 2:
	print("Ryu venceu")
elif rok == 2:
	print("Ken venceu")
elif ror == 1 and rok == 1:
	print("empatou")

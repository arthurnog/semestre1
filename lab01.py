#Arthur Lucas da Silva Nogueira 213293
#O programa serve para calcular a circunferencia de um planeta baseado no angulo e na distancia entre duas localidades
#as respostas dadas sao em estadios e em kilometros
D = float(input())
A = float(input())
Ce = (D*360)/A
CKm = (D*176.4*360)/(A*1000)
print("%.1f" %Ce)
print("%.1f" %CKm)
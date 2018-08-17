#Arthur Lucas da Silva Nogueira 213293
#o programa busca calcular o valor a ser pago por uma viagem de staruber a partir da distancia entre dois pontos do numero de cupons de desconto e do numero de pontos rebeldes acumulados pelo passageiro
vi = float(input())
xi = float(input())
yi = float(input())
xf = float(input())
yf = float(input())
t = float(input())
cd = float(input())
pr = float(input())
d = (xf - xi) + (yf - yi)
VC = vi + d*t
VD = max(cd, (VC * pr/100))
VF = VC - VD
print("%.2f" %VF)
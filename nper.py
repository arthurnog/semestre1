punch = int(input())
cont = 1
soma = 0

while cont < punch:
 if punch%cont == 0:
     soma = soma + cont
     cont = cont + 1
 else:
     cont = cont + 1
if soma == punch:
  punch = punch * 3
#if punch == soma and punch == k
    #punch = punch * 3
print(punch)

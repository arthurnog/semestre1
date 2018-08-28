l = "lala"
matriz = []
matriz2 = []
matrizP = []
lis = []
while l.isdigit() == False:
    l = input()
    if l.isdigit() == True:
        break
    else:
        for i in range(len(l)):
            lis.append(l[i])
        matriz.append(lis)
        matriz2.append(lis)
        lis = []
if l.isdigit() == True:
    n = int(l)
for k in range(n+1):
    if k == 0:
        for i in range(len(matriz[0])):
            for j in range(len(matriz)):
                print(matriz[i][j], end = "")
            print("")
    else:
        for i in range(1, len(matriz[0])):
            matriz[i]=matriz2[i][:]
            for j in range(1, len(matriz)):
                h = 0
                if matriz[i][j] == "@":
                    if matriz[i-1][j] == "@":
                        h += 1
                    if matriz[i+1][j] == "@":
                        h += 1
                    if matriz[i][j+1] == "@":
                        h += 1
                    if matriz[i][j-1] == "@":
                        h += 1
                    if matriz[i-1][j-1] == "@":
                        h += 1
                    if matriz[i-1][j+1] == "@":
                        h += 1
                    if matriz[i+1][j-1] == "@":
                        h += 1
                    if matriz[i+1][j+1] == "@":
                        h += 1
                    if h >= 4 or h <= 1:
                        matriz2[i][j] = " "
                if matriz[i][j] == " ":
                    if matriz[i-1][j] == "@":
                        h += 1
                    if matriz[i+1][j] == "@":
                        h += 1
                    if matriz[i][j+1] == "@":
                        h += 1
                    if matriz[i][j-1] == "@":
                        h += 1
                    if matriz[i-1][j-1] == "@":
                        h += 1
                    if matriz[i-1][j+1] == "@":
                        h += 1
                    if matriz[i+1][j-1] == "@":
                        h += 1
                    if matriz[i+1][j+1] == "@":
                        h += 1
                    if h == 3:
                        matriz2[i][j] = "@"
        matriz = matriz2[:]
        for i in range(len(matriz[0])):
            for j in range(len(matriz)):
                print(matriz[i][j], end = "")
            print("")

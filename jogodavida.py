l = "lala"
matriz = []
matriz2 = []
matrizP = []
lis = []
lista = []
while l.isdigit() == False:
    l = input()
    if l.isdigit() == True:
        break
    else:
        lista.append(l)
        for i in range(len(l)):
            lis.append(l[i])
        matriz.append(lis)
        matriz2.append(lis)
        lis = []
if l.isdigit() == True:
    n = int(l)
for k in range(n):
    for i in range(1, len(matriz)):
        matriz[i]=matriz2[i][:]
        for j in range(1, len(matriz[0])):
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
    for i in range(len(matriz)):
        t = "".join(matriz[i])
        lista[i] += (" " + t)
for i in range(len(lista)):
    print(lista[i])

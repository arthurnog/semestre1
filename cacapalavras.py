'''
 7 8 9
 6 . 2
 5 4 3
'''
#funcoes recursivas que encontram a palavra completa
def busca2(matriz, pontos, palavra, i , j, ind):
    print("lala")
    if ind == len(palavra):
        return True
    print(palavra[ind],i+1)
    if palavra[ind] == matriz[i+1][j]:
        if busca2(matriz, pontos, palavra, i+1, j, ind+1) == True:
            print("lala")
            pontos[i+1][j] = palavra[ind]
            return True
        else:
            return False

def busca3(matriz, pontos, palavra, i , j, ind):
    if ind == len(palavra):
        return True
    if palavra[ind] == matriz[i+1][j+1]:
        if busca2(matriz, pontos, palavra, i+1, j+1, ind+1) == True:
            pontos[i+1][j+1] = palavra[ind]
            return True
        else:
            return False

def busca4(matriz, pontos, palavra, i , j, ind):
    if ind == len(palavra):
        return True
    if palavra[ind] == matriz[i][j+1]:
        if busca2(matriz, pontos, palavra, i, j+1, ind+1) == True:
            pontos[i][j+1] = palavra[ind]
            return True
        else:
            return False

def busca5(matriz, pontos, palavra, i , j, ind):
    if ind == len(palavra):
        return True
    if palavra[ind] == matriz[i-1][j+1]:
        if busca2(matriz, pontos, palavra, i-1, j+1, ind+1) == True:
            pontos[i-1][j+1] = palavra[ind]
            return True
        else:
            return False

def busca6(matriz, pontos, palavra, i , j, ind):
    if ind == len(palavra):
        return True
    if palavra[ind] == matriz[i-1][j]:
        if busca2(matriz, pontos, palavra, i-1, j, ind+1) == True:
            pontos[i-1][j] = palavra[ind]
            return True
        else:
            return False

def busca7(matriz, pontos, palavra, i , j, ind):
    if ind == len(palavra):
        return True
    if palavra[ind] == matriz[i-1][j-1]:
        if busca2(matriz, pontos, palavra, i-1, j-1, ind+1) == True:
            pontos[i-1][j-1] = palavra[ind]
            return True
        else:
            return False

def busca8(matriz, pontos, palavra, i , j, ind):
    if ind == len(palavra):
        return True
    if palavra[ind] == matriz[i][j-1]:
        if busca2(matriz, pontos, palavra, i, j-1, ind+1) == True:
            pontos[i][j-1] = palavra[ind]
            return True
        else:
            return False

def busca9(matriz, pontos, palavra, i , j, ind):
    if ind == len(palavra):
        return True
    if palavra[ind] == matriz[i+1][j-1]:
        if busca2(matriz, pontos, palavra, i+1, j-1, ind+1) == True:
            pontos[i+1][j-1] = palavra[ind]
            return True
        else:
            return False

#funcao de buscar palavras na matriz
def busca(matriz, pontos, palavra):
    status=False
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if palavra[0] == matriz[i][j]:
                if busca2(matriz, pontos, palavra, i, j, 1) or busca3(matriz, pontos, palavra, i, j, 1) or busca4(matriz, pontos, palavra, i, j, 1) or busca5(matriz, pontos, palavra, i, j, 1) or busca6(matriz, pontos, palavra, i, j, 1) or busca7(matriz, pontos, palavra, i, j, 1) or busca8(matriz, pontos, palavra, i, j, 1) or busca9(matriz, pontos, palavra, i, j, 1):
                    print("lili")
                    pontos[i][j] = palavra[0]
                    status= True
                else:
                    status= False
            else:
                status= False
    return status

#le matriz
l = "lala"
pos = 0
matriz = []
resultado_final = []
m = []
while l.isdigit() == False:
    l = input()
    if l.isdigit() == True:
        break
    else:
        a = l.split()
        matriz.append([0]+a+[0])
        resultado_final.append('.')
matriz.append([0]*len(matriz[0]))
matriz.insert(0,[0]*len(matriz[0]))

# busca as palavras
if l.isdigit() == True:
    n = int(l)
#matriz de pontos
for i in range(len(matriz)):
    a = []
    for j in range(len(matriz[0])):
        a.append(".")
    m.append(a)
#buscando palavras
for k in range(n):
    word = input()
    busca(matriz, m, word)
#printa a matriz resposta
for i in range(1,len(m)-1):
    lis = []
    for j in range(1,len(m[0])-1):
        lis.append(m[i][j])
    stri = " ".join(lis)
    print(stri)

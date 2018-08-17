
#Arthur Lucas da Silva Nogueira
#213293
def hierarquia(matriz, n, funci, hier):
    count = 0
    for i in range(n):
        if matriz[funci][i] == 1:
            hier.append(i)
            hierarquia(matriz, n, i, hier)
        else:
            count += 1
    if count == n:
        return None

def ordem(vet):
    for i in range(len(vet)-1,0,-1):
        for j in range(i):
            if vet[j] > vet[j+1]:
                vet[j], vet[j+1] = vet[j+1], vet[j]
    return None

matriz = []
a = input()
dados = [int(i) for i in a.split()]
n = dados[0]
funci = dados[1]
#n=número de funcionarios; funci=funcionário que eu quero analizar
hier = []
#hier = lista com a hierarquia
for i in range(dados[0]):
    b = input()
    c = [int(i) for i in b.split()]
    matriz.append(c)
hierarquia(matriz, n, funci, hier)
ordem(hier)
hier = [funci]+hier
for i in range(len(hier)):
    hier[i] = str(hier[i])
print(" ".join(hier))

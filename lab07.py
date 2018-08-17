#Arthur Lucas da Silva Nogueira 213293
N = int(input())#esse númeor indica o tamanho da matriz
cont = 0#esse contador indica o numero de vezes que o * aparece na matriz
for i in range(1, N+1):#dentro desse looping eu verifico se  i divide j
    for j in range (1, N+1):#e aqui eu verifico se j divide i
        if i % j == 0 or j % i == 0:
            print("*", end="")#caso divida ele coloca um * na matriz e o contador e acrecentado mais 1
            cont += 1
        else:
            print("-", end="")#caso contrario ele coloca um - na matriz
    print("")
print(cont)#ao final eu imprimo o numero de asteriscos da matriz

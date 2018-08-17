
tabela = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(1, len(tabela)):
    aux = tabela[i]
    j = i - 1
    while(j>=0 and tabela[j][1]<aux[1]):
        tabela[j+1] = tabela[j]
        j = j - 1
    tabela[j+1] = aux
print(tabela)


    for i in range(1, len(tabela)):
        aux = tabela[i]
        j = i - 1
        while (j>=0 and tabela[j][1]<aux[1]):
            tabela[j+1] = tabela[j]
            j = j - 1
            if tabela[j][1] == aux[1] and tabela[j][2]<aux[2]:
                tabela[j+1] = tabela[j]
                j = j - 1
            if tabela[j][1] == aux[1] and tabela[j][2] == aux[2] and tabela[j][3]<aux[3]:
                tabela[j+1] = tabela[j]
                j = j - 1
            if tabela[j][1] == aux[1] and tabela[j][2] == aux[2] and tabela[j][3] == aux[3] and tabela[j][4]<aux[4]:
                tabela[j+1] = tabela[j]
                j = j - 1
        tabela[j+1] = aux
    return tabela

    tabela[j][1]<aux[1] or tabela[j][1] == aux[1] and tabela[j][2]<aux[2] or tabela[j][1] == aux[1] and tabela[j][2] == aux[2] and tabela[j][3]<aux[3] or tabela[j][1] == aux[1] and tabela[j][2] == aux[2] and tabela[j][3] == aux[3] and tabela[j][4]<aux[4]

        for i in range(1, len(tabela[1])):
            j = i - 1
            while j>=0:
                aux = []
                if tabela[i][1]>tabela[j][1]:
                    aux = tabela[i]
                    tabela[i] = tabela[j]
                    tabela[j] = aux
                    j = j - 1
                if tabela[i][1]<tabela[j][1]:
                    break
                if tabela[i][1] == tabela[j][1] and tabela[i][2]>tabela[j][2]:
                    aux = tabela[i]
                    tabela[i] = tabela[j]
                    tabela[j] = aux
                    j = j - 1
                if tabela[i][1] == tabela[j][1] and tabela[i][2]<tabela[j][2]:
                    break
                if tabela[i][1] == tabela[j][1] and tabela[i][2] == tabela[j][2] and tabela[i][3]>tabela[j][3]:
                    aux = tabela[i]
                    tabela[i] = tabela[j]
                    tabela[j] = aux
                    j = j - 1
                if tabela[i][1] == tabela[j][1] and tabela[i][2] == tabela[j][2] and tabela[i][3]<tabela[j][3]:
                    break
                if tabela[i][1] == tabela[j][1] and tabela[i][2] == tabela[j][2] and tabela[i][3] == tabela[j][3] and tabela[i][4]>tabela[j][4]:
                    aux = tabela[i]
                    tabela[i] = tabela[j]
                    tabela[j] = aux
                    j = j - 1
                if tabela[i][1] == tabela[j][1] and tabela[i][2] == tabela[j][2] and tabela[i][3] == tabela[j][3] and tabela[i][4]<tabela[j][4]:
                    break

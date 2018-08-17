#Arthur Lucas da silva Nogueira 213293
RAs = input()#RA dos alunos
lista = [int(i) for i in RAs.split()]
option = input()#opcao escolhida
opcao = option.split()
#******************************************************************************
#******************************************************************************
while opcao != 's':
    listac = lista[:]#lista ordenada em ordem crescente
    for i in range(1, len(listac)):
        aux = listac[i]
        j = i - 1
        while (j>=0 and listac[j] > aux):
            listac[j+1] = listac[j]
            j = j - 1
        listac[j+1] = aux
    listad = lista[:]#lista ordenada em ordem decrescente
    for i in range(1, len(listad)):
        aux = listad[i]
        j = i - 1
        while (j>=0 and listad[j] < aux):
            listad[j+1] = listad[j]
            j = j - 1
        listad[j+1] = aux
    if opcao[0] == 'p':
        #se a opcao for p ele imprime a lista de ras do jeito que ele foi criada
        for i in range(len(lista)):
            lista[i] = str(lista[i])
        sep = ' '
        lis = sep.join(lista)
        print(lis)
        option = input()
        opcao = option.split()
    elif opcao[0] == 'c':
        #se a opcao for c a lista deve ser ordenada em ordem crescente
        lista = listac
        option = input()
    elif opcao[0] == 'd':
        #se a opcao for d a lista deve ser ordenada em ordem decrescente
        lista = listad
        opcao = input()
    elif opcao[0] == 'b':
        ini=0
        fim=len(lista)-1
        st=''#o que deve ser printado quando a funcao for executada
        if (lista != listac) and (lista != listac):
            print("Vetor nao ordenado!")
        else:
            if int(opcao[1]) not in lista:
                print("%d nao esta na lista!"%(int(opcao[1])))
            else:
                if lista == listac:
                    while ini <= fim:
                        meio = (ini + fim)//2
                        if lista[meio] == int(opcao[1]):
                            st = st + str(meio)
                            print("%d esta na posicao: %d"%(int(opcao[1]), lista.index(int(opcao[1]))))
                        elif lista[meio] > int(opcao[1]):
                            fim = meio - 1
                            st = st + str(meio)
                        else:
                            ini = meio + 1
                            st = st + str(meio)
                if lista == listad:
                    while ini <= fim:
                        meio = (ini + fim)//2
                        if lista[meio] == int(opcao[1]):
                            st = st + str(meio)
                            print("%d esta na posicao: %d"%(int(opcao[1]), lista.index(int(opcao[1]))))
                        elif lista[meio] < int(opcao[1]):
                            fim = meio - 1
                            st = st + str(meio)
                        else:
                            ini = meio + 1
                            st = st + str(meio)
                print(st)
        option = input()
        opcao = option.split()
    elif opcao[0] == 'i':
        #se a opcao um ra deve ser inserido na lista
        if len(lista) == 150:
            print("Limite de vagas excedido!")
        else:
            if int(opcao[1]) in lista:
                print("Aluno ja matriculado na turma!")
            else:
                if (lista != listac) and (lista != listac):
                    lista.append(int(opcao[1]))
                elif lista == listac:
                    for i in range(len(lista)):
                        if int(opcao[1]) < lista[i]:
                            lista.insert(i, int(opcao[1]))
                            break
                elif lista == listad:
                    for i in range(len(lista)):
                        if int(opcao[1]) > lista[i]:
                            lista.insert(i, int(opcao[1]))
                            break
        option = input()
        opcao = option.split()
    elif opcao[0] == 'r':
        #encontra e remove um item da lista
        if lista == []:
            print("Nao ha alunos cadastrados na turma!")
        elif int(opcao[1]) not in lista:
            print("Aluno nao matriculado na turma!")
        else:
            del lista[lista.index(int(opcao[1]))]
        option = input()
        opcao = option.split()

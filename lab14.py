#Arthur Lucas da silva Nogueira 213293
RAs = input()#RA dos alunos
lista = [int(i) for i in RAs.split()]
for i in range(len(lista)):
    lista[i] = str(lista[i])
option = input()#opcao escolhida
opcao = option.split()
#******************************************************************************
while opcao[0] != 's':
    listac = lista[:]#lista ordenada em ordem crescente
    for i in range(1, len(listac)):
        aux = int(listac[i])
        j = i - 1
        while (j>=0 and int(listac[j]) > aux):
            listac[j+1] = int(listac[j])
            j = j - 1
        listac[j+1] = aux
    if listac != []:
        listac[0] = int(listac[0])
    listad = lista[:]#lista ordenada em ordem decrescente
    for i in range(1, len(listad)):
        aux = int(listad[i])
        j = i - 1
        while (j>=0 and int(listad[j]) < aux):
            listad[j+1] = int(listad[j])
            j = j - 1
        listad[j+1] = aux
    if listad != []:
        listad[0] = int(listad[0])
#******************************************************************************
    if opcao[0] == 'p':
        #se a opcao for p ele imprime a lista de ras do jeito que ele foi criada
        if lista == []:
            option = input()#opcao escolhida
            opcao = option.split()
        else:
            for i in range(len(lista)):
                lista[i] = str(lista[i])
            sep = ' '
            lis = sep.join(lista)
            print(lis + ' ')
            option = input()#opcao escolhida
            opcao = option.split()
#******************************************************************************
    elif opcao[0] == 'c':
        #se a opcao for c a lista deve ser ordenada em ordem crescente
        lista = listac[:]
        option = input()#opcao escolhida
        opcao = option.split()
#******************************************************************************
    elif opcao[0] == 'd':
        #se a opcao for d a lista deve ser ordenada em ordem decrescente
        lista = listad[:]
        option = input()#opcao escolhida
        opcao = option.split()
#******************************************************************************
    elif opcao[0] == 'b':
        listaint = [int(i) for i in lista]
        flag = 0
        ini=0
        fim=len(lista)-1
        st=[]#o que deve ser printado quando a funcao for executada
        if (listaint != listac) and (listaint != listad):
            print("Vetor nao ordenado!")
            flag = 1
        else:
            if listaint == listac:
                while ini <= fim:
                    meio = (ini + fim)//2
                    k = ("%d"%meio)
                    if listaint[meio] == int(opcao[1]):
                        st.append(k)
                        pr = " ".join(st)
                        print(pr + ' ')
                        print("%d esta na posicao: %d"%(int(opcao[1]), listaint.index(int(opcao[1]))))
                        flag = 1
                        break
                    if ini == fim:
                        st.append(k)
                        pr = " ".join(st)
                        print(pr + ' ')
                        flag = 1
                        print("%d nao esta na lista!"%(int(opcao[1])))
                        break
                    if listaint[meio] > int(opcao[1]):
                        fim = meio - 1
                        st.append(k)
                    elif listaint[meio] < int(opcao[1]):
                        ini = meio + 1
                        st.append(k)
            elif listaint == listad:
                while ini <= fim:
                    meio = (ini + fim)//2
                    k = ("%d"%meio)
                    if listaint[meio] == int(opcao[1]):
                        st.append(k)
                        pr = " ".join(st)
                        print(pr + ' ')
                        print("%d esta na posicao: %d"%(int(opcao[1]), listaint.index(int(opcao[1]))))
                        flag = 1
                        break
                    elif ini == fim:
                        st.append(k)
                        pr = " ".join(st)
                        print(pr + ' ')
                        print("%d nao esta na lista!"%(int(opcao[1])))
                        flag = 1
                        break
                    elif listaint[meio] < int(opcao[1]):
                        fim = meio - 1
                        st.append(k)
                    elif listaint[meio] > int(opcao[1]):
                        ini = meio + 1
                        st.append(k)
        if flag == 0:
            pr = " ".join(st)
            print(pr + ' ')
            print("%d nao esta na lista!"%(int(opcao[1])))

        option = input()#opcao escolhida
        opcao = option.split()
#******************************************************************************
    elif opcao[0] == 'i':
        #se a opcao um ra deve ser inserido na lista
        if len(lista) == 150:
            print("Limite de vagas excedido!")
        else:
            if str(opcao[1]) in lista:
                print("Aluno ja matriculado na turma!")
            else:
                listaint = [int(i) for i in lista]
                if (listaint != listac) and (listaint != listad):
                    lista.append(int(opcao[1]))
                elif listaint == listac:
                    for i in range(len(lista)):
                        if int(opcao[1]) < listaint[i]:
                            lista.insert(i, str(opcao[1]))
                            break
                    if int(opcao[1]) > int(lista[len(lista) - 1]):
                        lista.append(opcao[1])
                elif listaint == listad:
                    for i in range(len(lista)):
                        if int(opcao[1]) > listaint[i]:
                            lista.insert(i, str(opcao[1]))
                            break
                    if int(opcao[1]) < int(lista[len(lista) - 1]):
                        lista.append(opcao[1])
        option = input()#opcao escolhida
        opcao = option.split()
#******************************************************************************
    elif opcao[0] == 'r':
        #encontra e remove um item da lista
        if lista == []:
            print("Nao ha alunos cadastrados na turma!")
        elif str(opcao[1]) not in lista:
            print("Aluno nao matriculado na turma!")
        else:
            del lista[lista.index(str(opcao[1]))]
        option = input()#opcao escolhida
        opcao = option.split()
    if opcao[0] == 's':
        break

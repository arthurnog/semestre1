#Arthur Lucas da Silva Nogueira 213293
#D - apagar
#I - inverter
#R - substituir
#Q - sair do programa
discurso = str(input())
opcao = str(input())
print(discurso)
while opcao != 'Q':
    j = 0
    discurso1 = discurso.lower()#discurso com todas as letras minusuculas
    if opcao == 'R':#substituir uma palavra
        a = str(input())#palavra que vai ser subtituida
        b = str(input())#palavra que vai entrar no lugar da primeira
        a.lower()
        discurso1 = discurso1.split(" ")
        discurso = discurso.split(" ")
        k = [i for i,x in enumerate(discurso1) if x == a or x==a[1:len(x)] or x[0:len(x)-1] == a]#lista com as posições das palavras que vão sofrer alteração
        for i in k:
            if discurso[i+j][len(discurso[i+j])-1] in ['.','!','?',',',':']:#pontuacao nao retirada
                b = b + discurso[i+j][len(discurso[i+j])-1]
            discurso[i] = b
            j = j - 1
        discurso = ' '.join(discurso)
        discurso1 = ' '.join(discurso1)
    if opcao == 'I':#inverter uma palavra
        c1 = str(input())#palavra que vai ser invertida
        c3 = c1.lower()
        discurso1 = discurso1.split(" ")
        discurso = discurso.split(" ")
        k = [i for i,x in enumerate(discurso1) if x == c3 or x==c3[1:len(x)] or x[0:len(x)-1] == c3]
        for i in k:
            c2 = discurso[i][::-1]#aqui a palavra digitada é invertida
            if discurso[i+j][len(discurso[i+j])-1] in ['.','!','?',',',':']:#pontuacao nao retirada
                c2 = c2.replace(c2[0],"")
                c2 = c2 + discurso[i+j][len(discurso[i+j])-1]
            discurso[i] = c2
        discurso = ' '.join(discurso)
        discurso1 = ' '.join(discurso1)
    if opcao == 'D':#deletar uma palavra
        d = str(input())#palavra que vai ser retirada da string
        d = d.lower()
        discurso1 = discurso1.split(" ")
        discurso = discurso.split(" ")
        f = [i for i,x in enumerate(discurso1) if x == d or x==d[1:len(x)] or x[0:len(x)-1] == d]
        for i in f:
            if discurso[i+j][len(discurso[i+j])-1] in ['.','!','?']:#ponto final, exclamacao e interrogacao nao sao retiradas
                discurso[i+j-1] = discurso[i+j-1] + discurso[i+j][len(discurso[i+j])-1]
            del discurso[i+j]
            j = j - 1
        discurso = ' '.join(discurso)
        discurso1 = ' '.join(discurso1)
    opcao = str(input())
    print(discurso)

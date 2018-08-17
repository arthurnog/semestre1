#Arthur Lucas da Silva Nogueira 213293
#este programa tem a finalidade de calcular a media de mc102 fazendo uma media ponderada das notas das provas e da nota de laboratorio e caso nao se obtenha nota suficiente  a nota de exame e levada em consideracao na media final do aluno
P1 = float(input())
P2 = float(input())
Ml = float(input())
Mp = (2*P1 + 3*P2)/5
if Mp >= 5.0 and Ml >= 5.0:
    M = (3*Mp + 2*Ml)/5
    F = M
else:
    M = min(Mp, 4.9)
    if M >= 2.5 and M < 5:
        E = float(input())
        F = (M + E)/2
    else:
        F = M
print("%.1f" %Mp)
print("%.1f" %M)
print("%.1f" %F)
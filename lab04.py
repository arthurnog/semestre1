C = int(input())
a = 9
while a != 0:
    a = int(input())
    if a > 0 and a <= C:
        C = C - a
        print("Seja bem-vindo! Capacidade restante: %d" %C)
    elif a < 0:
        C = C - a
        print("Volte sempre! Capacidade restante: %d" %C)
    elif a > C:
        print("Veiculo muito grande! Capacidade restante: %d" %C)
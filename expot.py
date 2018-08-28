a = int(input())
b = int(input())
def pot(a, b):
    c = 1
    for i in range(b):
        c = c*a
    return c
r = pot(a, b)
print(r)

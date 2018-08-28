punch = int(input())
lst = []
a = 0
for i in range(1,200):
    a += i
    lst.append(a)
if punch in lst:
    print("numero triangular")
else:
    print("não é triangular")

hit = 0
ror = 0
rok = 0
rt = 2
ryu = 50
ken = 50
while rt != 0:
    punch = int(input())
    while punch > 0:
        hit = hit + punch
        if hit >= ken:
            rt = rt - 1
            ror = ror + 1
            print("Ken: %d" %ken + " - %d" %hit + " = %d" %(ken - hit))
            hit = 0
            ryu = 50
            ken = 50
            if ror == 2:
                print("ryu venceu")
        punch = int(input())
    if hit > 0:
        ken = ken - hit
        if ken <= 0:
            rt = rt -1
            ror = ror +1
            if punch < 0:
                print("Ken: %d" %ken + " - %d" %hit + " = %d" %(ken - hit))
            hit = 0
            ryu = 50
            ken = 50
    while punch < 0:
        hit = hit + punch
        if hit <= (-1 * ryu):
            rt = rt - 1
            rok = rok + 1
            if punch > 0:
                print("Ryu: %d" %ryu + " - %d" %(-1 * hit) + " = %d" %(ryu + hit))
            hit = 0
            ryu = 50
            ken = 50
            if rok == 2:
                print("Ryu: %d" %ryu + " - %d" %(-1 * hit) + " = %d" %(ryu + hit))
        punch = int(input())
    if hit < 0:
        ryu = ryu + hit
        if ryu <= 0:
            rt = rt -1
            rok = rok +1
            if punch > 0:
                print("ryu bla bla bla")
            hit = 0
            ryu = 50
            ken = 50
if ror == 2:
    print("ryu venceu")
elif rok == 2:
    print("ken venceu")
elif ror == 1 and rok == 1:
    print("empatou")

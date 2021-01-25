def hanoi(n, fr, tmp, to):
    if n==1:
        print("원판 1: %s --> %s" % (fr, to))
    else:
        hanoi(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n,fr,to))
        hanoi(n-1, tmp, fr, to)
hanoi(4, 'A','B','C')

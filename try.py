with open('27-B.txt') as f:
    n = int(f.readline())
    razn = 1000
    minsum = 0
    chet = 0
    nechet = 0
    for i in range(n):
        a, b = map(int, f.readline().split())
        minsum += min(a, b)
        q = abs(a - b)
        if min(a, b) % 2:
            nechet += 1
        else:
            chet += 1
        if q % 2 != 0 and q < razn:
            razn = q
    if (minsum% 2 == 0 and nechet >chet) or (minsum % 2 != 0 and chet > nechet):
        minsum += razn
    print(minsum)

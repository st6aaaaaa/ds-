def reverseBits(n):
    p = 31
    res = 0
    while n :
        r = n & 1
        res = res + (r << p)
        p -= 1
        n = n >> 1
    print(res)


reverseBits(43261596)


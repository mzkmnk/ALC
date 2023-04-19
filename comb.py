def comb(n,r):
    if n < r: return 0
    if r == 0: return 1
    if r > n-r:
        r = n-r
    num = 1
    den = 1
    for i in range(1,r+1):
        num *= n-r+i
        den *= i
    return num//den
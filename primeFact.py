#これは素因数分解をする関数
#Counterで何がいくつあるかカウントし
#print(prime_factorize(n))で素因数分解した値をリストに格納して返す
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
#cnt = collections.Counter(prime_factorize(n))
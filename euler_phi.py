from math import gcd
#上記の文は必要に応じて削除あり
def euler_phi(n):
    count = 0
    coprime_numbers = []
    for i in range(1,n+1):
        if gcd(n,i) == 1:
            count += 1
            coprime_numbers.append(i)
    return count,coprime_numbers
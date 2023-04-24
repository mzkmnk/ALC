def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        ex_gcd, x, y = extended_gcd(b, a % b)
        return ex_gcd, y, x - (a // b) * y
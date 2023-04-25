from itertools import groupby
N = int(input())
A = [(k, len(list(g))) for k, g in groupby(map(int, input().split()))]
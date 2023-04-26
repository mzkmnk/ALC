from itertools import groupby
from itertools import groupby
#N,は文字列の数,Sは文字列
def RLE(N, S):
    return [(k, len(list(g))) for k, g in groupby(S)]

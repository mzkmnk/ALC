def langless(N,S):
    langless = []
    idx = 0
    tmp = 1
    while idx < N:
        if idx + 1 >= N:
            break
        if S[idx] != S[idx+1]:
            langless.append(tmp)
            tmp = 0
        idx += 1
        tmp += 1
    langless.append(tmp)
    return langless
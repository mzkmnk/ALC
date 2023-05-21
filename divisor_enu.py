N = 10
arr = set()
i = 1
while(i*i <= N):
    if(N%i == 0):
        arr.add(i)
        if(i != N//i):
            arr.add(N//i)
    i+=1
print(arr)


def inserted(val):
    l  = len(val)
    for i in range(1, l):
        key = val[i]
        j = i-1
        while j >= 0 and key < val[j]:
            val[j+1] = val[j]
            j -= 1
        val[j] = key
    return val


val = list(map(int,input().split()))
done = inserted(val)
print(done)
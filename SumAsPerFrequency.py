from collections import Counter
N = int(input())                  # Reading input from STDIN
arr = list(map(int,input().split()))
freq = Counter(arr)
len_mx = max(freq.values())+1
lst = [0]*len_mx
for k,v in freq.items():
    lst[v] += k*v


for i in range(1,len_mx):
    lst[i] = lst[i-1]+lst[i]

Q = int(input())
for query in range(Q):
    l,r = map(int,input().split())
    if r >= len_mx:
        print(lst[len_mx-1]-lst[l-1])
    else:
        print(lst[r] - lst[l - 1])
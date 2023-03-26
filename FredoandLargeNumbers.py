from sys import stdin


def check_freq(ty,f,K,Y,sor_Y,mx,x):
    if f > mx:
        return 0

    elif ty == 0:
        for k,v in x.items():
            if v >= f:
                return k
    elif f in sor_Y:
        return K[Y.index(f)]
    return 0


N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
x = {}
for i in A:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1

K = [x.keys()]
Y = [x.values()]
sor_Y = set(Y)
mx = max(sor_Y)

Q = int(stdin.readline())

for _ in range(Q):
    ty, f = (map(int, stdin.readline().split()))
    print(check_freq(ty,f,K,Y,sor_Y,mx,x))


# print('Hi, %s.' % name)         # Writing output to STDOUT
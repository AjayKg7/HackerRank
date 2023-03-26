n, m = map(int, input().split())  # Reading input from STDIN
menus = [list(map(int, input().split())) for i in range(n)]
mxs = [0]*n
ind = 0
avg = 0

for i in range(m):
    x = menus[0][i]
    for j in range(n):
        if menus[j][i] > x:
            x = menus[j][i]
    for k in range(n):
        if menus[k][i] == x:
            mxs[k]+=1

mx_mxs = max(mxs)
for i in range(n):
    if mxs[i] == mx_mxs:
        a_val = sum(menus[i]) / m
        if a_val > avg:
            ind = i
            avg = a_val
print(ind + 1)

# print('Hi, %s.' % name)         # Writing output to STDOUT
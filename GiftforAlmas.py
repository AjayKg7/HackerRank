N = int(input())  # Reading input from STDIN
x = []
for _ in range(N):
    x.append(list(map(int, input().split())))
pos = input()
val = abs(pos.count('R') - pos.count('L'))
val = val % 4
if val == 0:
    for i in range(N):
        for k in x[i]:
            print(k, end=" ")
        print()
else:
    if pos.count('R') < pos.count('L'):
        if val == 1:
            val = 3
        elif val == 3:
            val = 1
    if val == 1:
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = x[i][j]
                x[i][j] = x[N - 1 - j][i]
                x[N - 1 - j][i] = x[N - 1 - i][N - 1 - j]
                x[N - 1 - i][N - 1 - j] = x[j][N - 1 - i]
                x[j][N - 1 - i] = temp
        for i in range(N):
            for k in x[i]:
                print(k, end=" ")
            print()

    elif val == 2:
        for i in range(N - 1, -1, -1):
            for k in x[i][::-1]:
                print(k, end=" ")
            print()
    elif val == 3:
        for row in x:
            row.reverse()
        for i in range(N):
            for j in range(i):
                x[i][j], x[j][i] = x[j][i], x[i][j]
        for i in range(N):
            for k in x[i]:
                print(k, end=" ")
            print()

# print('Hi, %s.' % name)         # Writing output to STDOUT
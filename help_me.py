
T = int(input())                  # Reading input from STDIN

for _ in range(T):
    M,K = map(int,input().split())
    S = input()

    if K > int(S):
        print(int(S))
    else:
        n = list(map(int, S.strip()))

        n.reverse()

        m = 1

        x, y, z = [], [], []

        for i in range(M):
            x.append(m)

            y.append(n[i] * m)

            m = (m * 10) % K

        T_sum = sum(y) % K

        s = (T_sum - y[M - 1]) % K

        z.extend([T_sum, s])

        for i in range(M - 2, -1, -1):
            s = (s - x[i] * (n[i] - n[i + 1])) % K

            z.append(s)

        print(max(z))


#print('Hi, %s.' % name)         # Writing output to STDOUT
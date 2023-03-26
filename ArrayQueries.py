def array_queries(N, M, A, B, Q, queries):

    sum_A = sum(A)
    sum_B = sum(B)
    sumAI = sum([(i + 1) * v for i, v in enumerate(A)])
    sumBJ = sum([(j + 1) * val for j, val in enumerate(B)])
    all_sum = [((sumAI * sum_B) + (sumBJ * sum_A)) % 998244353]
    for query in queries:
        i = query[1] - 1
        j = query[2] - 1
        if query[0] == 1:
            sum_A = sum_A - A[i] + B[j]
            sum_B = sum_B - B[j] + A[i]
            sumAI = sumAI - ((i + 1) * A[i]) + ((i + 1) * B[j])
            sumBJ = sumBJ - ((j + 1) * B[j]) + ((j + 1) * A[i])
            A[i], B[j] = B[j], A[i]

            all_sum.append(((sumAI * sum_B) + (sumBJ * sum_A)) % 998244353)

        elif query[0] == 2:
            sumAI = sumAI - ((i + 1) * A[i]) - ((j + 1) * A[j]) + ((i + 1) * A[j]) + ((j + 1) * A[i])
            A[i], A[j] = A[j], A[i]
            all_sum.append(((sumAI * sum_B) + (sumBJ * sum_A)) % 998244353)

        elif query[0] == 3:
            sumBJ = sumBJ - ((i + 1) * B[i]) - ((j + 1) * B[j]) + ((i + 1) * B[j]) + ((j + 1) * B[i])
            B[i], B[j] = B[j], B[i]
            all_sum.append(((sumAI * sum_B) + (sumBJ * sum_A)) % 998244353)

        else:
            pass
    return all_sum


T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for i in range(Q)]

    out_ = array_queries(N, M, A, B, Q, queries)
    print(' '.join(map(str, out_)))
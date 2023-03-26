def possible(array, L):
    init = array[0][0]
    final = array[0][1]
    tem_init = init
    for i in array:

        if final - init == L:
            return "Yes"
        else:
            if i[0] == final:
                final = i[1]
                tem_init = i[0]
            else:

                if i[0] == tem_init:
                    pass
                else:
                    init = i[0]
                    final = i[1]

    if final - init == L:
        return "Yes"
    return "No"


T = int(input())  # Reading input from STDIN

for each_test in range(T):
    N, L = map(int, input().split())
    array = []
    for i in range(N):
        x = list(map(int, input().split()))
        array.append(x)

    for k in range(N):
        for m in range(N - k - 1):
            if array[m][0] > array[m + 1][0]:
                array[m], array[m + 1] = array[m + 1], array[m]
            elif array[m][0] == array[m + 1][0]:
                if array[m][1] > array[m + 1][1]:
                    array[m], array[m + 1] = array[m + 1], array[m]


    res = possible(array, L)
    print(res)

# print('Hi, %s.' % name)         # Writing output to STDOUT
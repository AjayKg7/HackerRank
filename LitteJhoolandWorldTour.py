
def possible(N,ls):
    end = N - 1
    countries = []
    yes = True
    for i in ls:
        X, Y = i
        if yes:
            if X==Y or (X>Y+N):
                yes = False

    if yes:
        return "YES"
    return "NO"





T = int(input())  # Reading input from STDIN

for _ in range(T):
    N, M = (map(int, input().split()))
    # isit = True
    # end = N - 1
    # countries = []

    ls = [(map(int, input().split())) for i in range(M)]
    print(possible(N,ls))

    # for i in ls:
    #     X, Y = i
    #
    #     if X > end or Y > end:
    #         print("NO")
    #         isit = False
    #         break
    #
    #     elif X == Y:
    #         if X not in countries:
    #             countries.append(X)
    #         else:
    #             isit = False
    #             print("NO")
    #             break
    #     else:
    #         while X != Y + 1:
    #             if X == end:
    #                 if X not in countries:
    #                     countries.append(X)
    #                     possible = True
    #                     isit = True
    #                     # print(countries)
    #                     break
    #                 else:
    #                     X = 0
    #                     possible = False
    #                     isit = False
    #             else:
    #                 if X not in countries:
    #                     countries.append(X)
    #                     possible = True
    #                     isit = True
    #                     # print(countries)
    #                     break
    #                 else:
    #                     X += 1
    #                     possible = False
    #                     isit = False
    #         # print(countries)
    #         if not possible:
    #             print("NO")
    #             break
    # if isit:
    #     print("YES")

# print('Hi, %s.' % name)         # Writing output to STDOUT
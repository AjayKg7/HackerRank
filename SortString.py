def binsort(N,bin_str):
    zeros = bin_str.count('0')
    to_check = bin_str[:zeros]
    ones = to_check.count('1')
    return ones


T = int(input())
for test in range(T):
    N = int(input())
    bin_str = input()
    attempts = binsort(N,bin_str)
    print(attempts)
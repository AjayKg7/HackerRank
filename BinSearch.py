import timeit


def search(val,lst):
    lst = sorted(lst)

    while True:
        mid = len(lst) // 2
        print(mid, lst)
        if lst[mid-1] == val:
            print(lst[mid-1],val)
            break
        else:

            if lst[mid] <= val:
                lst = lst[mid:]
            else:
                lst = lst[:mid]

x=[i for i in range(0,10000000)]
strt = timeit.timeit()
res = search(8485,x)
end = timeit.timeit()
print(f'time taken is {end-strt}')
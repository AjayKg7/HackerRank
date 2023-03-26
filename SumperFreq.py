N = int(input())                  # Reading input from STDIN
arr = list(map(int,input().split()))

Q = int(input())
arr2 = set(arr)
times = []
sum_val = []
for i in arr2:
    x = arr.count(i)
    sum_val.append(x*i)
    times.append(x)

for i in range(1,len(times)):
    key = times[i]
    key2 = sum_val[i]
    j = i-1
    while j >= 0 and key < times[j]:
        times[j+1] = times[j]
        sum_val[j+1] = sum_val[j]
        j -= 1
    times[j+1] = key
    sum_val[j+1]=key2

for query in range(Q):
    l,r = map(int,input().split())
    count2=0

    for k,v in zip(times,sum_val):
        if k >= l :
            if k <= r:
                count2+=v
            else:
                break

    print(count2)

# stored_dict = {}
# for i in arr2:
#     x=arr.count(i)
#
#     if x in stored_dict:
#         stored_dict[x]+=(x*i)
#     else:
#         stored_dict[x] = (x*i)
#
# s_keys = [x for x in stored_dict.keys()]
# for i in range(1,len(s_keys)):
#     key = s_keys[i]
#     j = i-1
#     while j >= 0 and key < s_keys[j]:
#         s_keys[j+1] = s_keys[j]
#         j -= 1
#     s_keys[j+1] = key
#
# # print(s_keys, stored_dict)
# stored_dict2 = {key: stored_dict[key] for key in list(s_keys)}
#
# # print(stored_dict2)
# for query in range(Q):
#     l,r = map(int,input().split())
#     count2=0
#
#     for k,v in stored_dict2.items():
#         if k >= l :
#             if k <= r:
#                 count2+=v
#             else:
#                 break
#
#     print(count2)
#



# print('Hi, %s.' % name)         # Writing output to STDOUT
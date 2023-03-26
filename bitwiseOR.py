



lst = [1,3,4,1,5,6,7,3]

temp_lst = []
duplicates = []
for val in lst:
    if val in temp_lst:
        duplicates.append(val)
    else:
        temp_lst.append(val)
print(duplicates)
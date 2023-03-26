nums = []
count = 0
for i in range(44,1000000):
    x=str(i)
    val = True
    for j in x:
        if j in ['4','5']:
            val = True
        else:
            val = False
            break
    if val:
        nums.append(int(i))
        count+=1

print("The number of special nums present are :", count)
print(nums)


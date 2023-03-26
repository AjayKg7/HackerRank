
Y = [1,4,5,8,9,12]
z=[1,3,4,6,7,9]
f=5
md = len(Y)//2
print(md)
while Y[md] != f:
    if md == 0:
        print(0)
    elif Y[md] > f:
        Y = Y[:md]
        z = z[:md]
        md = md//2
    else:
        Y = Y[md+1:]
        z = z[md+1:]
        md = md // 2
print(md,Y[md],z[md],f)
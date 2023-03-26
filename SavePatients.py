def savepatients(N,strength, patients):

    for i in range(N):
        if strength(i) < patients(i):
            return "No"
    return "Yes"


N = int(input())                  # Reading input from STDIN
strength = list(map(int,input().split()))
patients = list(map(int,input().split()))

for i in range(N):
    for j in range(N-i-1):
        if strength[i] > strength[j+1]:
            strength[j],strength[j+1] = strength[j+1],strength[j]
        if patients[j] > patients[j+1]:
            patients[j], patients[j+1] = patients[j+1], patients[j]

res = savepatients(N,strength, patients)
print(res)

# print('Hi, %s.' % name)         # Writing output to STDOUT
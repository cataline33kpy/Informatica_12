A=[1,2,3,'A','B','C']
n=len(A)
for i in range(2**n):
    submultime=[]
    for j in range(n):
        if (i>>j)&1:
            submultime.append(A[j])
    print(set(submultime))     
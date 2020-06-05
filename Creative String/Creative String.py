from collections import Counter
n,k=map(int,input().split(" "))
li,s,ne=[],[],[]
for _ in range(n):
    li.append(list(input()))
z=list(zip(*li))
for i in range(k):
    p=sorted(list(z[i]))
    x=Counter(p)
    most=x.most_common(1)
    print(most[0][0],end="")

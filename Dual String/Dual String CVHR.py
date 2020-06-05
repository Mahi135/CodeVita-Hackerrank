#Dual String
def LCS(X, m):
    maxLength = 0
    lookup = [[0 for x in range(m + 1)] for y in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(i+1, m + 1):
            if X[i - 1] == X[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
                if lookup[i][j] > maxLength:
                    maxLength = lookup[i][j]
    return maxLength
for _ in range(int(input())):
    x=input()
    if(len(x)<2):
        print("No")
    else:
        sub=LCS(x,len(x))
        res=len(x)-2*sub
        if(res==len(x)):
            print("No")
        else:
            print("Yes")

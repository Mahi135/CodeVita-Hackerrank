for _ in range(int(input())):
    x=[]
    y=[]
    for i in range(int(input())):
        v=list(map(int,input().split()))
        x.append(v[0])
        y.append(v[1])
    if (abs(min(x)-max(x)))**2>(abs(min(y)-max(y)))**2 or (abs(min(x)-max(x)))**2==(abs(min(y)-max(y)))**2:
        print(abs(min(x)-max(x)))**2)
    else:
        print(abs(min(y)-max(y)))**2)

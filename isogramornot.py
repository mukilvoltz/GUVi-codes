a=str(input())
lett=list(a)
c=0
d=0
for x in lett:
    n=lett.index(x)
    for i in range(n+1,len(a)):
        if x==lett[i]:
            print("No")
            c=1
            d=1
            break
    if d==1:
        break
if c==0:
    print("Yes")

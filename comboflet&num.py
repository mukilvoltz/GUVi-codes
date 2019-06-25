a=str(input())
b=list(a)
c=0
d=0
for x in b:
    if x.isalpha():
        c=c+1
    else:
        d=d+1
if c>0 and d>0:
    print("Yes")
else:
    print("No")

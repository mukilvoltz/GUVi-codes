a,b=input().split()
a=list(a)
b=int(b)
n=len(a)
index=n-b
for i in range (index,n):
    print(a[i],end="")

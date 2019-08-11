a=input()
n=len(a)
a=int(a)
b=0
b2=0
ans=0
for i in range(0,n):
    b=a%10
    b2=b**2
    ans=ans+b2
    a=int(a/10)
print(ans)

p,q=input().split()
p=int(p)
q=int(q)
def arm(a):
    a=str(a)
    n=len(a)
    a=int(a)
    q=a
    s=0
    t=0
    for  i in range(0,n):
        t=a%10
        t=t**3
        s=s+t
        a=a//10
    if s == q:
        print(q, end =" ")
for i in range (p+1,q):
    arm(i)

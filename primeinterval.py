p,q=input().split()
p=int(p)
q=int(q)
def prime(a):
    n=int(a/2)
    c=0
    for i in range (2,n+1):
        if a % i == 0:
            c=1
            break
    if c == 0:
        print(a, end =" ")
for j in range (p+1,q):
    prime(j)

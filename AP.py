n,a,d=input().split()
a=int(a)
n=int(n)
d=int(d)
s=0
for i in range(1,n):
    s=(a+(n-1)*d)+s
print(s)

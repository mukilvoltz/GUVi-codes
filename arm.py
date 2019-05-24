a=str(input())
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
    print("yes")
else:
    print("no")

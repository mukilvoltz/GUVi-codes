a=str(input())
q=a
n=len(a)
a=int(a)
s=0
t=""
for i in range(0,n):
    s=a%10
    s=str(s)
    t=t+s
    a=a//10
    s=int(s)
if t == q:
    print("yes")
else:
    print("no")

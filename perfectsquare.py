a,b=input().split()
a=int(a)
b=int(b)
c=a*b
d=0
e=0
i=0
while(d<=c):
    d=i**2
    if d == c:
        print("yes")
        e=1
        break
    i=i+1
if e == 0:
    print("no")

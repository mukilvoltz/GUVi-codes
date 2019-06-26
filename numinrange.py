a=int(input())
b,c=input().split()
b=int(b)
c=int(c)
if a>b and a<c:
    print("yes")
elif a<b and a>c:
    print("yes")
else:
    print("no")

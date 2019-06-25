l,m=input().split()
l=int(l)
m=int(m)
arr=[int(x) for x in input().split()]
c=0
for i in arr:
    if i == m:
        print("yes")
        c=1
        break
if c == 0:
    print("no")

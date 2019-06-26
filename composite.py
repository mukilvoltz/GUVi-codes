a=int(input())
n=int(a/2)
c=0
for i in range (2,n+1):
    if a % i == 0:
        c=1
        print("yes")
        break
if c == 0:
    print("no")

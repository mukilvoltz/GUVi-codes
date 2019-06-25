n,k=input().split()
n=int(n)
k=int(k)
arr=[int(x) for x in input().split()]
c=0
for i in arr:
    if i == k:
        c=c+1
print(c)

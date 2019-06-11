p,q=input().split()
p=int(p)
q=int(q)
s=0
arr = [int(x) for x in input().split()]
for i in range (0,q):
    s=s+arr[i]
print(s)

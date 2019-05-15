a,b=input().split()
b=int(b)
c=0
arr = list(map(int, input().split()))
for i in range (0,b):
    c=arr[i]+c
print(c)

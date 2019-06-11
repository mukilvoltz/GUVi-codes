max=0
p=int(input())
arr=[int(x) for x in input().split()]
for i in arr:
    for j in range(0,p):
        if i>arr[j]:
            max=i
print(max)

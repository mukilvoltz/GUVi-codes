max=0
p=int(input())
arr=[int(x) for x in input().split()]
for i in arr:
    for j in range(0,p):
        if i>arr[j]:
            if max<i:
                max=i
min=arr[0]
for k in arr:
    for l in range(0,p):
        if k<arr[l]:
            if k<min:
                min=k
print(min, end=" ")
print(max)

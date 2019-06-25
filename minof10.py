arr=[int(x) for x in input().split()]
min=arr[0]
for i in arr:
    for j in range(0,10):
        if i<arr[j]:
            if i<min:
                min=i
print(min)

p,q=input().split()
q=int(q)
arr=[int(x) for x in input().split()]
min=arr[0]
inde=0
k=1
while(k<=q):
    for i in arr:
        for j in range(0,len(arr)):
            if i<arr[j]:
                if i<min:
                    min=i
    if k<q:
        arr.remove(min)
        min=arr[0]
    k=k+1
print(min)

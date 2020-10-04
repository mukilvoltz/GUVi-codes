arr=[int(x) for x in input().split()]
alarr=[]
n=arr[0]
arr.pop(0)
g=arr[0]
s=arr[0]
for i in range(0,len(arr)):
    if len(arr)!=0:
        for j in range(0,len(arr)):
            if arr[j]>g:
                g=arr[j]
        alarr.append(g)
        print(arr)
        if len(arr)!=0:
            arr.pop(arr.index(g))
        for k in range(0,len(arr)):
            if arr[k]<s:
                s=arr[k]
        alarr.append(s)
        if len(arr)!=0:
            arr.pop(arr.index(s))
        if len(arr)!=0:
            g=arr[0]
            s=arr[0]
for i in range(0,len(alarr)-1):
    print(alarr[i], end=" ")

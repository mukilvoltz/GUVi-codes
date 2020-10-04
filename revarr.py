n=int(input())
arr=[int(x) for x in input().split()]
for i in range(len(arr)-1,0,-1):
    print(arr[i],end=" ")
print(arr[0],end="")

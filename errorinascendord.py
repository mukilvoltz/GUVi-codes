a=int(input())
arr=[int(x) for x in input().split()]
b=0
c=0
for i in range(0,a-1):
    b=arr[i]
    c=arr[i+1]
    if b>c:
        print(i)
        break

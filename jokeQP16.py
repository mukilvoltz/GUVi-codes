a=int(input())
arr=[int(x) for x in input().split()]
for i in arr:
    if arr.count(i)==1:
        print(i)
        break

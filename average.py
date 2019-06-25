su=0
a=int(input())
arr=[int(x) for x in input().split()]
for i in arr:
    su=su+i
print(int(su/a))

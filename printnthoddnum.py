a,b=input().split()
b=int(b)
arr=[int(x) for x in input().split()]
ary=[]
for i in arr:
    if i%2!=0:
        ary.append(i)
print(ary[b-1])

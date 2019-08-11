a=str(input())
ans=''
max=0
for x in a:
    if a.count(x)>max:
        max=a.count(x)
        ans=x
print(ans)

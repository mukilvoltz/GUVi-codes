a=int(input())
b=str(input())
vow=['a','e','i','o','u']
c=''
for i in b:
    if i not in vow:
        c=c+i
print(c[::-1])

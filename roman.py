a=str(input())
n=len(a)
s=0
for i in range(0,n):
    if a[i] == "X":
        s=s+10
    elif a[i] == "V":
        s=s+5
    elif a[i] == "I":
        s=s-1
print(s)    
